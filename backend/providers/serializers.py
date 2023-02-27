from rest_framework import serializers
from .models import Provider


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ['id', 'user_id', 'first_name', 'last_name',
                  'phone', 'address', 'email', 'business_description', 'payment_type']
        depth = 1
