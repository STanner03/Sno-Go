from rest_framework import serializers
from .models import Provider


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ['id', 'user_id', 'first_name', 'last_name',
                  'phone', 'address', 'email', 'equipment_id', 'services_id', 'business_description', 'payment_type']
        depth = 1
