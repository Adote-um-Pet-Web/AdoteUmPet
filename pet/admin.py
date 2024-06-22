from django.contrib import admin

from . import models


class MedicalRecordInline(admin.StackedInline):
    model = models.MedicalRecord
    extra = 1


class ImagesPetInline(admin.StackedInline):
    model = models.ImagesPets
    extra = 1


class HistoryPetInline(admin.StackedInline):
    model = models.HistoryPet
    extra = 1


@admin.register(models.BannerImagens)
class BannerImagensAdmin(admin.ModelAdmin):
    list_display = (
        "banner_image1_thumbnail",
        "banner_image2_thumbnail",
        "banner_image3_thumbnail",
        "banner_image1_name",
        "banner_image2_name",
        "banner_image3_name",
    )

    def banner_image1_name(self, obj):
        return obj.banner_image1.name.split("/")[-1] if obj.banner_image1 else ""

    banner_image1_name.short_description = "Banner Image 1 Name"

    def banner_image2_name(self, obj):
        return obj.banner_image2.name.split("/")[-1] if obj.banner_image2 else ""

    banner_image2_name.short_description = "Banner Image 2 Name"

    def banner_image3_name(self, obj):
        return obj.banner_image3.name.split("/")[-1] if obj.banner_image3 else ""

    banner_image3_name.short_description = "Banner Image 3 Name"


@admin.register(models.Pet)
class PetAdmin(admin.ModelAdmin):
    inlines = [MedicalRecordInline, ImagesPetInline, HistoryPetInline]
    list_display = (
        "name",
        "species",
        "breed",
        "age",
        "adopted",
        "profile_image_thumbnail",
    )
    search_fields = ("name", "species", "breed")
    list_filter = ("species", "sex", "size", "adopted", "created_at")

    def profile_image_thumbnail(self, obj):
        images_pets = obj.images_pets.first()
        if images_pets:
            return images_pets.image_pet_profile_thumbnail()
        return ""

    profile_image_thumbnail.short_description = "Profile Image"
