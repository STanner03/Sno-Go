from django.db import models
from authentication.models import User
from equipment.models import Equipment


# Create your models here.

class Provider(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=75)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    services = models.CharField(max_length=255)
    business_description = models.CharField(max_length=255)
    payment_type = models.CharField(max_length=255)