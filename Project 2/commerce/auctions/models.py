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
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    highest_bid = models.IntegerField(default=0, null=True)
    def __str__(self):
        return f"{self.title}"