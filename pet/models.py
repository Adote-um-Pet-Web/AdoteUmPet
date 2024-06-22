import uuid

from django.db import models
from django.utils.html import format_html

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
    size = models.CharField(max_length=20, choices=Size.choices)
    weight = models.IntegerField()
    heigth = models.IntegerField()
    adopted = models.BooleanField(default=False)
    favorited = models.BooleanField(default=False)
    adoption = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class HistoryPet(models.Model):
    id_pet = models.ForeignKey(
        Pet, on_delete=models.CASCADE, related_name="history_pet"
    )
    history = models.TextField(
        default="Nenhuma historia foi adicionado", blank=True, null=True
    )
    observations = models.TextField(
        default="Nenhuma historia foi adicionado", blank=True, null=True
    )


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

    def image_pet_profile_thumbnail(self):
        if self.image_pet_profile:
            return format_html(
                '<img src="{}" style="width: 45px; height:45px;" />'.format(
                    self.image_pet_profile.url
                )
            )
        return ""

    image_pet_profile_thumbnail.short_description = "Profile Image"


class FavoritedPet(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="favorited_pets"
    )
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="favorited_by")
    favorited = models.BooleanField(default=False)

    class Meta:
        unique_together = ("user", "pet")


class AdoptionPets(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="adoption_pets"
    )
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="adoption_by")
    adoption = models.BooleanField(default=False)

    class Meta:
        unique_together = ("user", "pet")


# Create your models here.
class BannerImagens(models.Model):
    banner_image1 = models.ImageField(
        upload_to="banner/imagens/%Y/%m/", blank=False, null=False
    )
    banner_image2 = models.ImageField(
        upload_to="banner/imagens/%Y/%m/", blank=False, null=False
    )
    banner_image3 = models.ImageField(
        upload_to="banner/imagens/%Y/%m/", blank=False, null=False
    )

    def banner_image1_thumbnail(self):
        if self.banner_image1:
            return format_html(
                '<img src="{}" style="width: 45px; height:45px;" />'.format(
                    self.banner_image1.url
                )
            )
        return ""

    banner_image1_thumbnail.short_description = "Banner Image 1"

    def banner_image2_thumbnail(self):
        if self.banner_image2:
            return format_html(
                '<img src="{}" style="width: 45px; height:45px;" />'.format(
                    self.banner_image2.url
                )
            )
        return ""

    banner_image2_thumbnail.short_description = "Banner Image 2"

    def banner_image3_thumbnail(self):
        if self.banner_image3:
            return format_html(
                '<img src="{}" style="width: 45px; height:45px;" />'.format(
                    self.banner_image3.url
                )
            )
        return ""

    banner_image3_thumbnail.short_description = "Banner Image 3"
