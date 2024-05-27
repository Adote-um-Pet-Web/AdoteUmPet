from django import forms
from .models import Pet, HistoryPet, MedicalRecord, ImagesPets, Image


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'species', 'breed', 'age', 'color', 'sex', 'size', 'weight', 'adopted']

class HistoryPetForm(forms.ModelForm):
    class Meta:
        model = HistoryPet
        fields = ['history', 'observations']

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['castreated', 'vaccines', 'vaccine_description', 'dewormed', 'dewormer_description', 'medical_history']


from multiupload.fields import MultiFileField

class ImagesPetsForm(forms.ModelForm):
    class Meta:
        model = ImagesPets
        fields = ['id_pet', 'image_profile', 'image_pets']
