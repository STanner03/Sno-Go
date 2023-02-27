from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from .models import Service
from .serializers import ServiceSerializer
from providers.models import Provider

# Create your views here.

def staff_member_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='admin:login'):
    """
    Decorator for views that checks that the user is logged in and is a staff
    member, redirecting to the login page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_staff,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator

@api_view(['Get'])
@permission_classes([AllowAny])
def get_all_services(request):
    services = Service.objects.all()
    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data)


@api_view(['Get'])
@permission_classes([AllowAny])
def get_providers_services(request, ppk):
    services = Service.objects.filter(providers=ppk)
    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def update_providers_services(request, ppk, pk):
    service = get_object_or_404(Service, pk=pk)
    provider = get_object_or_404(Provider, pk=ppk)
    if request.method == 'PUT':
        provider.services.add(service)
        serializer = ServiceSerializer(service, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(id=pk)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        provider.services.remove(service)
        return Response("Success", status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@staff_member_required()
def add_services(request):
    if request.method == 'POST':
        serializer = ServiceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
@staff_member_required()
def update_service(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'PUT':
        serializer = ServiceSerializer(service, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
