from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.

from .serializers import TasksSerializer
from .models import TaskToUser

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def task_list(request):
    user = request.user
    task = TaskToUser.objects.filter(user = user)
    seralizer = TasksSerializer(task, many = True)
    
    return Response(seralizer.data, status=status.HTTP_200_OK)