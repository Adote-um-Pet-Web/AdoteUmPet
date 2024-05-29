import uuid

from django.db import models

from userauth.models import User


class Species(models.TextChoices):
    DOG = "DOG", "Dog"
    CAT = "CAT", "Cat"


class Sex(models.TextChoices):
    Male = "Male", "Macho"
    Female = "Female", "Femea"


class Size(models.TextChoices):
    Small = "SMALL", "Pequeno"
    Medio = "MEDIUM", "Medio"
    Large = "Large", "Grande"


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
    size =  models.CharField(max_length=20, choices=Size.choices)
    weight =  models.IntegerField()
    heigth =  models.IntegerField()
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
    castreated = models.BooleanField(blank=True, null=True)
    vaccines = models.BooleanField(blank=True, null=True)
    vaccine_description = models.TextField(blank=True, null=True)
    dewormed = models.BooleanField(blank=True, null=True)
    dewormer_description = models.TextField(blank=True, null=True)
    medical_history = models.TextField(blank=True, null=True)


class ImagesPets(models.Model):
    id_pet = models.ForeignKey(
        Pet, on_delete=models.CASCADE, related_name="images_pets"
    )
    image_pet_profile = models.ImageField(upload_to="pets/profile/%Y/%m/")
    image_pet_datail1 = models.ImageField(upload_to="pets/photos/%Y/%m/")
    image_pet_datail2 = models.ImageField(upload_to="pets/photos/%Y/%m/")
    image_pet_datail3 = models.ImageField(upload_to="pets/photos/%Y/%m/")
