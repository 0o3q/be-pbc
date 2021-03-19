from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to="%Y%m%d", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content = models.CharField(max_length=200)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE, blank=True)
