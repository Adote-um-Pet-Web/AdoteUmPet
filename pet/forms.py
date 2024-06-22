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
            "heigth",
            "weight",
            "adopted",
        ]

    def clean_name(self):
        name = self.cleaned_data["name"]
        if any(char.isdigit() for char in name):
            raise forms.ValidationError("O nome não pode conter números.")
        return name

    def clean_color(self):
        color = self.cleaned_data["color"]
        if any(char.isdigit() for char in color):
            raise forms.ValidationError("A cor não pode conter números.")
        return color

    def clean_breed(self):
        breed = self.cleaned_data["breed"]
        if any(char.isdigit() for char in breed):
            raise forms.ValidationError("A raça não pode conter números.")
        return breed

    def clean_age(self):
        age = self.cleaned_data["age"]
        if not str(age).isdigit():
            raise forms.ValidationError("A idade deve ser um número positivo.")
        if int(age) < 0:
            raise forms.ValidationError("A idade deve ser um número.")
        return age

    def clean_heigth(self):
        height = self.cleaned_data["heigth"]
        if not str(height).isdigit():
            raise forms.ValidationError("A altura deve ser um número positivo.")
        if int(height) < 0:
            raise forms.ValidationError("A altura deve ser um número.")
        return height

    def clean_weight(self):
        weight = self.cleaned_data["weight"]
        if not str(weight).isdigit():
            raise forms.ValidationError("O peso deve ser um número positivo.")
        if int(weight) < 0:
            raise forms.ValidationError("O peso deve ser um número.")
        return weight


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

    def clean_image_pet_profile(self):
        image = self.cleaned_data.get("image_pet_profile")
        if not image:
            raise forms.ValidationError("Carregue a imagem de perfil do pet.")
        return image

    def clean_image_pet_datail1(self):
        image = self.cleaned_data.get("image_pet_datail1")
        if not image:
            raise forms.ValidationError("Carregue a primeira imagem de detalhe do pet.")
        return image

    def clean_image_pet_datail2(self):
        image = self.cleaned_data.get("image_pet_datail2")
        if not image:
            raise forms.ValidationError("Carregue a segunda imagem de detalhe do pet.")
        return image

    def clean_image_pet_datail3(self):
        image = self.cleaned_data.get("image_pet_datail3")
        if not image:
            raise forms.ValidationError("Carregue a terceira imagem de detalhe do pet.")
        return image
