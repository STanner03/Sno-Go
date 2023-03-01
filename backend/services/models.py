from django.db import models

# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
