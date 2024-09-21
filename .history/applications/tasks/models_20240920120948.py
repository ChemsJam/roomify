from django.db import models
from django.contrib.auth.models import User
# Create your models here.

get_status = {
    ("CU","Current"),
    ("CO","Completed"),
    ("CAN","Canceled"),
    ("EX","Expired")
}

get_difficulty = {
    ("HRD","Hard"),
    ("MID","Middle"),
    ("EZ","Easy"),
}

class TaskList(models.Model):
    name = models.CharField("Name",max_length = 50)
    difficulty = models.CharField(max_length = 3, choices = get_difficulty)
    

class TaskToUsers(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    open_date = models.DateField(("Open date"), auto_now=True, auto_now_add=True)
    complete_date = models.DateField(("Completed date"), auto_now=False, auto_now_add=False, null=True)
    status = models.CharField(max_length=3, choices=get_status)
    
    