from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("details/<str:title>", views.details, name="details"),
    path("search", views.search, name="search"),
    path('create', views.create, name="create"),
    path('edit/<str:title>', views.edit, name="edit-page"),
    path('save', views.save_edit, name="save-edit"),
]