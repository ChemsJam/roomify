from rest_framework import serializers
from .models import TaskToUser, TaskList

from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields = ['id', 'name', 'difficulty']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # Aquí puedes elegir qué campos del usuario mostrar

class UserTaskSerializer(serializers.ModelSerializer):
    task = TaskSerializer(read_only=True)  # Anida el TaskSerializer para mostrar detalles completos de la tarea

    class Meta:
        model = TaskToUser
        fields = ['id', 'task', 'open_date', 'complete_date', 'status']