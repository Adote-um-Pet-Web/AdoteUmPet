from django.db import models
from django.contrib.auth.models import User
from utils.idrandom import random_id

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True, unique=True, default=random_id, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    role = models.CharField(max_length=255)


    def __str__(self):
        return self.name
