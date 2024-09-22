from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.

from .serializers import UserTaskSerializer, UserSerializer
from .models import TaskToUser

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def task_list(request):
    user = request.user
    user_serializer = UserSerializer(user)
    
    user_tasks = TaskToUser.objects.filter(user = user)
    task_serializer = UserTaskSerializer(user_tasks, many = True)
    
    response_data = {
        "user": user_serializer.data,  # Los datos del usuario se devuelven una sola vez
        "tasks": task_serializer.data   # La lista de tareas asociadas
    }
    
    return Response(response_data, status=status.HTTP_200_OK)