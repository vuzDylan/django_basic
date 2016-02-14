from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    name = models.CharField(max_length=100, unique=True)
    details = models.CharField(max_length=500)
    user = models.ForeignKey(User, related_name="todos")
    completed = models.BooleanField(default=False)
