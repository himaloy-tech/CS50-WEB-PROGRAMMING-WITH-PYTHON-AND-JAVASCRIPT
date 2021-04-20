from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    desc = models.TextField()
    def __str__(self) -> str:
        return f"{self.title}"

class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='thumbnails')
    desc = models.TextField()
    title = models.TextField(default="")
    category = models.TextField(default="")
    posts = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="posts", blank=True, null=True, default="")
    id = models.AutoField(primary_key=True)
    def __str__(self) -> str:
        return f"{self.title}"

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField()
    message = models.TextField()
    email = models.EmailField()
    datetime = models.DateTimeField(auto_now_add=True)