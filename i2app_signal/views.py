from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import CategorySerializer, DeviceSerializer, TaskSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DeviceViewset(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]


class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
