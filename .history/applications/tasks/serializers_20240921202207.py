from rest_framework import serializers
from .models import TaskToUser, TaskList

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskToUser
        fields = ['id', 'user', 'task', 'open_date', 'complete_date', 'status']