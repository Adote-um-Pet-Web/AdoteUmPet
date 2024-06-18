from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import User


class UserLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Digite o seu email"}),
        error_messages={
            "required": "Este campo é obrigatório.",
            "invalid": ("Informe um endereço de email válido."),
        },
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Senha"}),
        error_messages={"required": "Este campo é obrigatório."},
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError(("Email ou senha incorretos."))
        return cleaned_data


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Nome Completo"}),
        error_messages={
            "required": _("Este campo é obrigatório."),
            "max_length": _("O nome deve ter no máximo 150 caracteres."),
        },
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Email"}),
        error_messages={
            "required": _("Este campo é obrigatório."),
            "invalid": _("Insira um endereço de email válido."),
        },
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Senha"}),
        error_messages={
            "required": _("Este campo é obrigatório."),
        },
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Confirme a senha"}),
        error_messages={
            "required": _("Este campo é obrigatório."),
        },
    )
    image_user_profile = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={"id": "fileInput", "class": "custom-file-input"}),
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "phone_number",
            "password1",
            "password2",
            "image_user_profile",
        ]

    def clean_username(self):
        username = self.cleaned_data["username"].lower()

        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError(_("Este email já está em uso."))
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(_("As senhas não coincidem."))
        return password2

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password1 = cleaned_data.get("password1")

        if password1:
            if email and email.split("@")[0].lower() in password1.lower():
                self.add_error("password1", _("A senha é muito parecida com o email."))
            if len(password1) < 8:
                self.add_error(
                    "password1",
                    _("Esta senha é muito curta. Deve conter pelo menos 8 caracteres."),
                )

        return cleaned_data


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Nome Completo"}),
        error_messages={
            "required": _("Este campo é obrigatório."),
            "max_length": _("O nome deve ter no máximo 150 caracteres."),
        },
    )
    facebook_field = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Facebook"}),
    )
    instagram_field = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Instagram"}),
    )
    phone_number = forms.CharField(
        widget=forms.NumberInput(attrs={"placeholder": "Número de Telefone"}),
        error_messages={
            "required": _("Este campo é obrigatório."),
            "invalid": _("Insira um número de telefone válido."),
        },
    )

    class Meta:
        model = User
        fields = ["username", "facebook_field", "phone_number", "instagram_field"]


class UserProfileImageUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["image_user_profile"]
        widgets = {
            "image_user_profile": forms.FileInput(
                attrs={"id": "fileInput", "class": "custom-file-input"}
            ),
        }
