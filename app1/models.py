import uuid

from django.contrib.auth.models import User
from django.db import models


class App(models.Model):
    name = models.CharField(max_length=50, default=uuid.uuid4)
    create_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
