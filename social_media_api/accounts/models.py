from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
#ashould contain: ["from django.contrib.auth.models import AbstractUser", "bio", "profile_picture", "followers", "models.ManyToManyField", "models.ImageField", "models.TextField"]


class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

    def __str__(self):
        return self.username