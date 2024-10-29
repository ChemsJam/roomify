# En el archivo urls.py de la app (por ejemplo, "tasks/urls.py")
from django.urls import path
from .views import task_list, task_create  # Importamos la vista task_list

urlpatterns = [
    path('tasks/', task_list, name='task-list'),
    path('createTask/', task_create, name='task-create'),
    path('assignTask/', task_list, name='task-list'),
    path('cancelTask/', task_list, name='task-list'),
    path('tradeTask/', task_list, name='task-list'),
    path('completeTask/', task_list, name='task-list'),
]