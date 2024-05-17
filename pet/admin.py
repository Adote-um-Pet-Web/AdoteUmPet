from django.contrib import admin

from . import models


class MedicalRecordLine(admin.StackedInline):
    model = models.MedicalRecord
    extra = 1


class ImagesPetsLine(admin.TabularInline):
    model = models.ImagesPets
    extra = 1


class MedicalRecordAdmin(admin.ModelAdmin): ...


class PetAdmins(admin.ModelAdmin):
    inlines = [MedicalRecordLine, ImagesPetsLine]


admin.site.register(models.Pet, PetAdmins)
admin.site.register(models.ImagesPets)
admin.site.register(models.MedicalRecord)
