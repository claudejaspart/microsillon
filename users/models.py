from django.db import models


# Create your models here.
class USER(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.CharField(max_length=10, blank=True, null=True)
    # password
    hash = models.CharField(max_length=255, blank=True, null=True)
    salt = models.CharField(max_length=255, blank=True, null=True)
    # user role
    role = models.IntegerField(null=True)
    # postal address
    street_number = models.CharField(max_length=50)
    street_name = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=100)