from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    body = models.TextField()
    datetime = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_follower")
    user_following = models.ManyToManyField(User, related_name="followers", blank=True)

    def __str__(self):
        return f"{self.user.username}"

class Following(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_following")
    user_following = models.ManyToManyField(User, related_name="following", blank=True)

    def __str__(self):
        return f"{self.user.username}"