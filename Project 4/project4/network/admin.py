from django.contrib import admin
from .models import User, Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ("user", "datetime")

admin.site.register(Post, PostAdmin)
admin.site.register(User)