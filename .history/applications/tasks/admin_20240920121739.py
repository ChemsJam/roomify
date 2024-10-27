from django.contrib import admin
from .models import TaskList, TaskToUsers

# Register your models here.
admin.site.register(TaskList, TaskToUsers)
