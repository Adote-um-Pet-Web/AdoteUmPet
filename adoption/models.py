from django.db import models

from pet.models import Pet
from userauth.models import User
from utils.idrandom import random_id


class Adoption(models.Model):
    id = models.IntegerField(
        primary_key=True, unique=True, default=random_id, editable=False
    )
    adopter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="adopted_pets"
    )
    pet = models.OneToOneField(Pet, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.pet.name
