from email.policy import default
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import requests
import random


class Post(models.Model) :
    querystring = {"name":"{body}"}
    headers = {
	"X-RapidAPI-Key": "7d6f0e6ddcmsh07cf4610b0f633ap1657a2jsn77b8367a1023",
	"X-RapidAPI-Host": "spotify-scraper.p.rapidapi.com"
}
    body = models.CharField(max_length= 6)
    image = models.ImageField(upload_to='uploads/post_photos', blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    rand = random.randrange(110000, 112024, 1)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    r = requests.get("https://spotify-scraper.p.rapidapi.com/v1/track/search", headers=headers, params=querystring)
    song = r.json()['shareUrl']
  

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=10, blank=True, null=True)
 
    bio = models.TextField(max_length=300, blank=True, null=True)
    location = models.CharField(max_length= 100, blank=True, null=True)
    picture = models.ImageField(upload_to='uploads/profile_pictures', default= 'uploads/profile_pictures/default.jpeg', blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()