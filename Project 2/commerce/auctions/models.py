from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listings(models.Model):
    """
    docstring
    """
    title = models.TextField()
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails')
    starting_bid = models.IntegerField()
    choices = (("Fashion", "Fashion"), ("Electronics", "Electronics"), ("Furniture", "Furniture"), ("Daily Essentials", "Daily Essentials"))
    category = models.CharField(max_length = 100, choices=choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title}"