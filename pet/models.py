from django.db import models
from userprofile.models import Profile
from utils.idrandom import random_id
class Species(models.TextChoices):
    DOG = 'DOG', 'Dog'
    CAT = 'CAT', 'Cat'
    # Add more species as needed


class Pet(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, default=random_id, editable=False)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='pets')
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=20, choices=Species.choices)
    breed = models.CharField(max_length=255)
    age = models.IntegerField()
    color = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    size = models.IntegerField()
    weight = models.IntegerField()
    history = models.TextField()
    observations = models.TextField()
    image_profile = models.ImageField(upload_to="pets/profile/imagesPets/%Y/%m/", blank=True, null=True)
    photos = models.CharField(max_length=255)
    adopted = models.BooleanField()

    def __str__(self):
        return self.name

class MedicalRecord(models.Model):
    id_pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='medical_records')
    castreated = models.BooleanField()
    vaccines = models.BooleanField()
    vaccine_description = models.TextField()
    dewormed = models.BooleanField()
    dewormer_description = models.TextField()
    medical_history = models.TextField()


class ImagesPets(models.Model):
    id_pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='ImagesPets')
    image_pets = models.ImageField(upload_to="pets/photos/imagesPets/%Y/%m/", blank=True, null=True)
