from django.db import models
import datetime as dt


class Project(models.Model):
    title = models.CharField(blank=False, max_length=200)
    url = models.CharField(blank=False, max_length=200)
    descrption = models.TextField(blank=False, max_length=500)
    technology = models.CharField(blank=True, max_length=200)
    image = models.ImageField(blank=False)
    


