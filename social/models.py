from email.policy import default
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Post(models.Model) :
    body = models.TextField()
    image = models.ImageField(upload_to='uploads/post_photos', blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=10, blank=True, null=True)
    bio = models.TextField(max_length=300, blank=True, null=True)
    location = models.CharField(max_length= 100, blank=True, null=True)
    picture = models.ImageField(upload_to='uploads/profile_pictures', default= 'uploads/profile_pictures/default.jpeg', blank=True)

