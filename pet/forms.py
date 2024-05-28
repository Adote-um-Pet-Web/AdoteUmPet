from django import forms

from .models import HistoryPet, ImagesPets, MedicalRecord, Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = [
            "name",
            "species",
            "breed",
            "age",
            "color",
            "sex",
            "size",
            "weight",
            "adopted",
        ]


class HistoryPetForm(forms.ModelForm):
    class Meta:
        model = HistoryPet
        fields = ["history", "observations"]


class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = [
            "castreated",
            "vaccines",
            "vaccine_description",
            "dewormed",
            "dewormer_description",
            "medical_history",
        ]


class ImagesPetsForm(forms.ModelForm):

    class Meta:

        model = ImagesPets

        fields = (
            "image_pet_profile",
            "image_pet_datail1",
            "image_pet_datail2",
            "image_pet_datail3",
        )
