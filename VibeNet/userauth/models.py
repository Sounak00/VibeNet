from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime
# Create your models here.

class Profile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    id_user=models.IntegerField(primary_key=True, default=0)
    bio=models.TextField(blank=True, default='')
    profileimg=models.ImageField(upload_to='profile_img/', default='blank-profile-picture.webp')
    location=models.CharField(max_length=100, blank=True,default='')

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4)
    user=models.CharField(max_length=100)
    image=models.ImageField(upload_to="post_images/", blank=True, null=True)
    captions=models.TextField()
    created_at=models.DateTimeField(default=datetime.now)
    no_of_likes=models.IntegerField(default=0)

    def __str__(self):
        return self.user
    
class LikePost(models.Model):
    post_id=models.CharField( max_length=500)
    username=models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
class Followers(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user
    
