from rest_framework import serializers
from .models import TaskToUser, TaskList

from django.contrib.auth.models import User

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields = ['id', 'name', 'description']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']  # Aquí puedes elegir qué campos del usuario mostrar

class UserTaskSerializer(serializers.ModelSerializer):
    task = TaskSerializer(read_only=True)  # Anida el TaskSerializer para mostrar detalles completos de la tarea
    user = UserSerializer(read_only=True)  # Anida el UserSerializer para mostrar detalles del usuario

    class Meta:
        model = TaskToUser
        fields = ['id', 'user', 'task', 'open_date', 'complete_date', 'status']