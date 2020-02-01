from django.db import models
from django.contrib.auth.models import  User

# Create your models here.
class UserProfile(models.Model):
    user        = models.OneToOneField(User,on_delete=models.CASCADE)
    location    = models.CharField(max_length=30,null=True, blank=True)
    address     = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return  self.user.username