from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Course, Contact
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

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        message = request.POST.get('message')
        email = request.POST.get('email')
        obj = Contact.objects.create(name=name, message=message, email=email, user=request.user)
        obj.save()
        messages.success(request, "Your Query has been Successfully Submitted")
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "contact.html")