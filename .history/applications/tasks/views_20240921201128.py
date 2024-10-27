from ...roomify.serialzers import UserSerializer
from django.contrib.auth.models import User
from .models import TaskToUser

# Create your views here.

@api_view(['POST'])
def task_list(request):
    