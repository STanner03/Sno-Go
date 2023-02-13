from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Provider
from .serializers import ProviderSerializer

# Create your views here.


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_providers(request):
    providers = Provider.objects.all()
    serializer = ProviderSerializer(providers, many=True)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_providers(request):
    if request.method == 'POST':
        serializer = ProviderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user_id=request.user.id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        providers = Provider.objects.filter(user_id=request.user.id)
        serializer = ProviderSerializer(providers, many=True)
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def update_provider(request, pk):
    provider = get_object_or_404(Provider, pk=pk)
    if request.method == 'PUT':
        serializer = ProviderSerializer(provider, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user_id=request.user.id)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        provider.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
