from django.test import TestCase

from userauth.forms import UserRegisterForm


class UserRegisterFormTestCase(TestCase):
    def test_form_valid_data(self):
        # Testa se o formulário é válido com dados válidos
        form_data = {
            "username": "testuser",
            "email": "test@example.com",
            "phone_number": "123456789",
            "password1": "testpassword",
            "password2": "testpassword",
        }
        form = UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        # Testa se o formulário é inválido com dados inválidos
        invalid_form_data = {
            "username": "",  # Nome de usuário em branco
            "email": "invalidemail",  # Email inválido
            "phone_number": "invalidnumber",  # Número de telefone inválido
            "password1": "short",  # Senha muito curta
            "password2": "password",  # Senhas não coincidem
        }
        form = UserRegisterForm(data=invalid_form_data)
        self.assertFalse(form.is_valid())

    def test_form_field_placeholders(self):
        # Testa se os placeholders estão configurados corretamente
        form = UserRegisterForm()
        self.assertEqual(
            form.fields["username"].widget.attrs["placeholder"], "Nome Completo"
        )
        self.assertEqual(form.fields["email"].widget.attrs["placeholder"], "Email")
        self.assertEqual(
            form.fields["phone_number"].widget.attrs["placeholder"],
            "Número de Telefone",
        )
        self.assertEqual(
            form.fields["password1"].widget.attrs["placeholder"], "Password"
        )
        self.assertEqual(
            form.fields["password2"].widget.attrs["placeholder"], "Confirm Password"
        )
