import uuid

from django.db import models

from userauth.models import User


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
    adopted = models.BooleanField()

    def __str__(self):
        return self.name


class HistoryPet(models.Model):
    id_pet = models.ForeignKey(
        Pet, on_delete=models.CASCADE, related_name="history_pet"
    )
    history = models.TextField(blank=True, null=True)
    observations = models.TextField(blank=True, null=True)


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
    id_pet = models.ForeignKey(
        Pet, on_delete=models.CASCADE, related_name="images_pets"
    )
    image_pet_profile = models.ImageField(upload_to="pets/profile/%Y/%m/")
    image_pet_datail1 = models.ImageField(upload_to="pets/photos/%Y/%m/")
    image_pet_datail2 = models.ImageField(upload_to="pets/photos/%Y/%m/")
    image_pet_datail3 = models.ImageField(upload_to="pets/photos/%Y/%m/")
