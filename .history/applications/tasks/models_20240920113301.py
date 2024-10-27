from django.db import models

# Create your models here.

class task(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    open_date = models.DateField(_("Open date"), auto_now=False, auto_now_add=False, null=True)
    complete_date = models.DateField(_("Completed date"), auto_now=False, auto_now_add=False)