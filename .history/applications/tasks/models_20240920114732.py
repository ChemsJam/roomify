from django.db import models

# Create your models here.

get_status = {
    ("CU","Current"),
    ("CO","Completed"),
    ("CAN","Canceled"),
    ("EX","Expired")
}

class task(models.Model):
    name = models.CharField(("Name"), max_length=50)
    open_date = models.DateField(("Open date"), auto_now=False, auto_now_add=False, null=True)
    complete_date = models.DateField(("Completed date"), auto_now=False, auto_now_add=False, null=True)
    status = models.CharField(max_length=3, choices=get_status)