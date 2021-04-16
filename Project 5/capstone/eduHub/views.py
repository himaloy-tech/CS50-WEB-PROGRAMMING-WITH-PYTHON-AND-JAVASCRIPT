from django import http
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Course
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request, "index.html", {
        "Course":Course.objects.all()
    })

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.error(request, "Invalid Credentials")
            return HttpResponseRedirect(reverse("login"))
    else:
        return render(request, "login.html")

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)
        user.save()
        auth_login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "register.html")
