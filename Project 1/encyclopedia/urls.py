from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("details/<str:title>", views.details, name="details"),
    path("search", views.search, name="search"),
]