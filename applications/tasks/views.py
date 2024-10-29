from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.

from .serializers import UserTaskSerializer, UserSerializer, TaskSerializer
from .models import TaskToUser, TaskList

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

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def task_create(request):
    # Inicializar el serializador con los datos de la solicitud
    task_serializer = TaskSerializer(data=request.data)
    
    # Validar los datos antes de usarlos
    if task_serializer.is_valid():
        # Guardar la tarea en la base de datos
        task_serializer.save()

        # Respuesta con los datos de la tarea creada
        response_data = {
            "message": "Task created successfully",
            "task": task_serializer.data
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
    
    # Si los datos no son válidos, devolver un error
    return Response(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)