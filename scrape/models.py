from django.db import models

# Create your models here.

class Link(models.Model):
    region_name = models.CharField(max_length=50)
    region_link = models.CharField(max_length=1000)
