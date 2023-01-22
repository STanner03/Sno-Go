from django.db import models
# from clients.models import Client
# from providers.models import Provider

# Create your models here.

class Job(models.Model):
    # client = models.ForeignKey(Client, on_delete=models.CASCADE)
    # provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    area_type = models.CharField(max_length=255)
    photo_required = models.BooleanField()
    recurring = models.BooleanField()
    cash_only = models.BooleanField()