from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'user_id', 'first_name', 'last_name',
                  'phone', 'address', 'email']
        depth = 1
