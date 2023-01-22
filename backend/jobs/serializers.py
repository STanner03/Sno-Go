from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'client_id', 'provider_id', 'address',
                  'area_type', 'photo_required', 'recurring', 'cash_only']
        depth = 1