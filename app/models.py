from django.db import models
from django.utils import timezone

# Create your models here.

class PcNames(models.Model):
    name = models.CharField(max_length=50)

class views(models.Model):
    views = models.IntegerField(default=0)
    date = models.DateField()
    PcNames = models.CharField(max_length=50, default='')
    
class todays_view(models.Model):
    views = models.IntegerField(default=0)
    date = models.DateField()