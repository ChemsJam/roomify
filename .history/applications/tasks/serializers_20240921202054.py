from rest_framework import serializers
from .models import TaskToUser, TaskList

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']