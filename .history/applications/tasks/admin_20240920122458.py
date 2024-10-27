from django.contrib import admin
from .models import TaskList, TaskToUser

# Register your models here.
admin.site.register(TaskList)
admin.site.register(TaskToUser)
