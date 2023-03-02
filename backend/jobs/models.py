from django.db import models
from clients.models import Client
from providers.models import Provider
from services.models import Service

# Create your models here.


class Job(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=255)
    services = models.ManyToManyField(Service, related_name="jobs")
    photo_required = models.BooleanField(null=True)
    recurring = models.BooleanField(null=True)
    cash_only = models.BooleanField(null=True)
    total_price = models.FloatField(null=True)
    date_requested = models.DateTimeField()
    date_completed = models.DateTimeField(null=True)
    paid = models.BooleanField(null=True)
