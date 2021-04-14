from django.shortcuts import render
from .models import Course
# Create your views here.

def index(request):
    course = Course.objects.all()
    print(course)
    return render(request, "index.html", {
        "Course":Course.objects.all()
    })