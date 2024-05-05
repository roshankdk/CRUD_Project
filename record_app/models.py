from asyncio.windows_events import NULL
from enum import unique
from django.db import models

# Create your models here.

class user(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(unique=True, max_length=20)

