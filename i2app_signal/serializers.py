from rest_framework import serializers
from . models import User, Category, Device, Task


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Category


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name', 'category']
        model = Device


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Task
