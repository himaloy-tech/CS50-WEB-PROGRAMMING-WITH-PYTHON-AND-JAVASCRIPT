from django.contrib import admin
from .models import Listings, User
# Register your models here.
admin.site.register(Listings)
admin.site.register(User)