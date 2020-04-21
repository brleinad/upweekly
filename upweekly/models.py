from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import datetime


class CompletedTask(models.Model):
    date = models.DateField(default=timezone.now())
    detail = models.CharField(max_length = 255)
    #highlight =  BooleadField(default=False)

    def __str__(self):
        return self.detail


#class PlannedTask(models.Model):
