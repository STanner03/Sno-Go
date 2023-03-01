from django.db import models
from authentication.models import User


# Create your models here.

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=75)
