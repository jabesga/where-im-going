from django.db import models
from django.contrib.auth.models import User
  
  
class Event(models.Model):
    name = models.CharField(max_length=256) 
    
class UserProfile(models.Model):
    user = models.ForeignKey(User, related_name="user")
    name = models.CharField(max_length=256)
    follow_to = models.ManyToManyField(User, related_name="follow_to")
    will_attend_to = models.ManyToManyField(Event)