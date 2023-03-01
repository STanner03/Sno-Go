from rest_framework import serializers
from .models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'client_id', 'provider_id', 'address',
                  'services', 'photo_required', 'recurring', 'cash_only', 'total_price', 'date_requested', 'date_completed', 'paid']
        depth = 1
