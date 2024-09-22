# En el archivo urls.py de la app (por ejemplo, "tasks/urls.py")
from django.urls import path
from .views import task_list  # Importamos la vista task_list

urlpatterns = [
    path('tasks/', task_list, name='task-list'),  # Definimos la ruta para listar las tareas
]
