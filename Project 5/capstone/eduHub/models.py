from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    desc = models.TextField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"{self.title}"

class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='thumbnails')
    desc = models.TextField()
    title = models.TextField(default="")
    category = models.TextField(default="")
    posts = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="posts")
    def __str__(self) -> str:
        return f"{self.title}"