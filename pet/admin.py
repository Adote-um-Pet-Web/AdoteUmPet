from django.contrib import admin

from . import models


class MedicalRecordLine(admin.StackedInline):
    model = models.MedicalRecord
    extra = 1


class ImagesPetsLine(admin.StackedInline):
    model = models.ImagesPets
    extra = 1


class HistoryPetLine(admin.StackedInline):
    model = models.HistoryPet
    extra = 1


class MedicalRecordAdmin(admin.ModelAdmin): ...


class PetAdmins(admin.ModelAdmin):
    inlines = [MedicalRecordLine, ImagesPetsLine, HistoryPetLine]


admin.site.register(models.Pet, PetAdmins)
admin.site.register(models.ImagesPets)
admin.site.register(models.MedicalRecord)
admin.site.register(models.HistoryPet)
