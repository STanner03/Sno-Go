from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Job
from .serializers import JobSerializer

# Create your views here.


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_jobs(request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_jobs(request):
    print('User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'POST':
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        jobs = Job.objects.filter(user_id=request.user.id)
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def update_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.method == 'PUT':
        serializer = JobSerializer(job, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user_id=request.user.id)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)