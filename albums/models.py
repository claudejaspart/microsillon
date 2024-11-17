from django.db import models

# Create your models here.
class ALBUM(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    artist = models.CharField(max_length=100, blank=True, null=True)
    release_year = models.IntegerField()
    tracks = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    images = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    stock = models.IntegerField(null=True)
