from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Task (models.Model):
    description = models.CharField(max_length = 200)
    completed = models.BooleanField(default = False)
    author = models.ForeignKey( User,  on_delete=models.PROTECT )# settings.AUTH_USER_MODEL,

    def __str__ (self):
        return self.description