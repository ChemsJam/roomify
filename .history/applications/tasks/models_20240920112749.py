from django.db import models

# Create your models here.

class task(models.Model):
    name = models.CharField(_("Name"), max_length=50)
     