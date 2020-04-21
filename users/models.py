from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """The user model for upweekly"""
    pass
    
