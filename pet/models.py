from django.db import models
import uuid
from userauth.models import User
from utils.idrandom import random_id


class Species(models.TextChoices):
    DOG = "DOG", "Dog"
    CAT = "CAT", "Cat"

class Sex(models.TextChoices):
    DOG = "Male", "Macho"
    CAT = "Female", "Femea"

class Pet(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pet")
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=20, choices=Species.choices)
    breed = models.CharField(max_length=255)
    age = models.IntegerField()
    color = models.CharField(max_length=255)
    sex = models.CharField(max_length=20, choices=Sex.choices)
    size = models.IntegerField()
    weight = models.IntegerField()
    history = models.TextField(blank=True, null=True)
    observations = models.TextField(blank=True, null=True)
    image_profile = models.ImageField(
        upload_to="pets/profile/imagesPets/%Y/%m/", blank=False, null=False
    )
    adopted = models.BooleanField()

    def __str__(self):
        return self.name


class MedicalRecord(models.Model):
    id_pet = models.ForeignKey(
        Pet, on_delete=models.CASCADE, related_name="medical_records"
    )
    castreated = models.BooleanField()
    vaccines = models.BooleanField()
    vaccine_description = models.TextField()
    dewormed = models.BooleanField()
    dewormer_description = models.TextField()
    medical_history = models.TextField()


class ImagesPets(models.Model):
    id_pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="ImagesPets")
    image_pets = models.ImageField(
        upload_to="pets/photos/imagesPets/%Y/%m/", blank=True, null=True
    )
