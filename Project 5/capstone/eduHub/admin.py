from django.contrib import admin
from .models import Course, Post, Contact, User
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'datetime')

admin.site.register(Course)
admin.site.register(Post)
admin.site.register(User)
admin.site.register(Contact, ContactAdmin)
