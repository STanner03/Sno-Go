from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Service
from .serializers import ServiceSerializer

# Create your views here.

@api_view(['Get'])
@permission_classes([AllowAny])
def get_all_services(request):
    services = Service.objects.all()
    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data)


@api_view(['Get'])
@permission_classes([AllowAny])
def get_providers_services(request, ppk):
    services = Service.objects.filter(provider_id=ppk)
    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_services(request, ppk):
    if request.method == 'POST':
        serializer = ServiceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user_id=request.user.id, provider_id=ppk)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        services = Service.objects.filter(user_id=request.user.id)
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def update_service(request, ppk, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'PUT':
        serializer = ServiceSerializer(service, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user_id=request.user.id, provider_id=ppk)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
