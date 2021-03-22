from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.db.models.aggregates import Count
from django.db.models.fields import PositiveSmallIntegerField
from django.db.models.query import prefetch_related_objects
from django.http import HttpResponseRedirect
from django.http.request import RawPostDataException
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import User, Post, Follower, Following


def index(request):
    posts = Post.objects.all().order_by('-datetime')
    return render(request, "network/index.html", {
        "posts":posts
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        follower = Follower(user=user)
        follower.save()
        following = Following(user=user)
        following.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

@login_required(login_url='/login')
def post(request):
    if request.method == "POST":
        body = request.POST.get("message")
        user = request.user
        post = Post(body=body, user=user)
        post.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/post.html")

def profile(request, username):
    buttton = True
    check = False
    posts = Post.objects.filter(user__username=username).order_by('-datetime')
    follower_obj = Follower.objects.filter(user__username=username)
    following_obj = Following.objects.filter(user__username=username)
    for follower_count in follower_obj :
        follower_count = follower_count.user_following.all().count()

    for following_count in following_obj:
        following_count = following_count.user_following.all().count()
    if request.user.username == username:
        buttton = False
    else:
        check = Following.objects.filter(user = request.user, user_following__username=username).exists()
    return render(request, "network/profile.html", {
        "posts": posts,
        "username": username,
        "follower_count": follower_count,
        "following_count": following_count,
        "button":buttton,
        "check":check
        })
@login_required(login_url="/login")
def follow(request, username):
    user = User.objects.get(username=username)
    followings = Following.objects.get(user=request.user)
    followings.user_following.add(user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url="/login")
def unfollow(request, username):
    user = User.objects.get(username=username)
    followings = Following.objects.get(user=request.user)
    followings.user_following.remove(user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))