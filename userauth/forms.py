from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Nome Completo"})
    )
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email"}))
    phone_number = forms.IntegerField(
        widget=forms.NumberInput(attrs={"placeholder": "Número de Telefone"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Senha"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Confirme a senha"})
    )

    image_user_profile = forms.ImageField(
    required=False,
    widget=forms.FileInput(attrs={"id": "fileInput", "class": "custom-file-input"}),

)


    class Meta:
        model = User
        fields = ["username", "email", "phone_number", "password1", "password2", "image_user_profile"]
