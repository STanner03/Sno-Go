from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from .models import Equipment
from .serializers import EquipmentSerializer
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
def get_all_equipment(request):
    equipment = Equipment.objects.all()
    serializer = EquipmentSerializer(equipment, many=True)
    return Response(serializer.data)


@api_view(['Get'])
@permission_classes([AllowAny])
def get_providers_equipment(request, ppk):
    equipment = Equipment.objects.filter(providers=ppk)
    serializer = EquipmentSerializer(equipment, many=True)
    return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def update_providers_equipment(request, ppk, pk):
    equip = get_object_or_404(Equipment, pk=pk)
    provider = get_object_or_404(Provider, pk=ppk)
    if request.method == 'PUT':
        add_equipment_to_provider = provider.equipment.add(equip)
        return Response(add_equipment_to_provider, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        remove_equipment_from_provider = provider.equipment.remove(equip)
        return Response(remove_equipment_from_provider, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@staff_member_required()
def add_equipment(request):
    if request.method == 'POST':
        serializer = EquipmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
@staff_member_required()
def update_equipment(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'PUT':
        serializer = EquipmentSerializer(equipment, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        equipment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
