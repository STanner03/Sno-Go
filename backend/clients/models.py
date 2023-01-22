from django.db import models

# Create your models here.

class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=75)