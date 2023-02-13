from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Equipment
from .serializers import EquipmentSerializer

# Create your views here.


@api_view(['Get'])
@permission_classes([AllowAny])
def get_all_equipment(request):
    equipment = Equipment.objects.all()
    serializer = EquipmentSerializer(equipment, many=True)
    return Response(serializer.data)


@api_view(['Get'])
@permission_classes([AllowAny])
def get_providers_equipment(request, ppk):
    equipment = Equipment.objects.filter(provider_id=ppk)
    serializer = EquipmentSerializer(equipment, many=True)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_equipment(request, ppk):
    if request.method == 'POST':
        serializer = EquipmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user_id=request.user.id, provider_id=ppk)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        equipment = Equipment.objects.filter(user_id=request.user.id)
        serializer = EquipmentSerializer(equipment, many=True)
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def update_equipment(request, ppk, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'PUT':
        serializer = EquipmentSerializer(equipment, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user_id=request.user.id, provider_id=ppk)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        equipment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
