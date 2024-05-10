from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from userauth.forms import UserRegisterForm

User = get_user_model()


class RegisterViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_register_view_get(self):
        response = self.client.get(reverse("userauths:sign-up"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "userauths/sign-up.html")

    def test_register_view_post_valid_data(self):
        data = {
            "username": "testuser",
            "email": "test@example.com",
            "phone_number": "123456789",
            "password1": "testpassword",
            "password2": "testpassword"
        }
        response = self.client.post(reverse("userauths:sign-up"), data)
        self.assertEqual(response.status_code, 302)  # Redirecionamento esperado após o registro
        self.assertTrue(User.objects.filter(email="test@example.com").exists())

    def test_register_view_post_invalid_data(self):
        # Testa postagem de dados inválidos
        data = {
            "username": "",
            "email": "invalidemail",
            "phone_number": "invalidnumber",
            "password1": "short",
            "password2": "password"
        }
        response = self.client.post(reverse("userauths:sign-up"), data)
        self.assertEqual(response.status_code, 200)  # O formulário é exibido novamente
        self.assertFormError(response, "form", "email", "Enter a valid email address")
        self.assertFormError(response, "form", "phone_number", "Enter a whole number.")

    def test_register_view_authenticated_user(self):
        # Testa se um usuário já autenticado é redirecionado corretamente
        user = User.objects.create_user(username="testuser", email="test@example.com", password="testpassword")
        self.client.force_login(user)
        response = self.client.get(reverse("userauths:sign-up"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("account:account"))


class LoginViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", email="test@example.com", password="testpassword")

    def test_login_view_get(self):
        response = self.client.get(reverse("userauths:sign-in"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "sign-in.html")

    def test_login_view_post_valid_data(self):
        data = {
            "email": "test@example.com",
            "password": "testpassword"
        }
        response = self.client.post(reverse("userauths:sign-in"), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(reverse("account:account")))

    def test_login_view_post_invalid_data(self):
        data = {
            "email": "invalidemail",
            "password": "testpassword"
        }
        response = self.client.post(reverse("userauths:sign-in"), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(reverse("userauths:sign-in")))
        self.assertContains(response, "Username or password does not exist")

    def test_login_view_authenticated_user(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("userauths:sign-in"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("account:account"))


class LogoutViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", email="test@example.com", password="testpassword")
        self.client.force_login(self.user)

    def test_logout_view(self):
        response = self.client.get(reverse("userauths:logout"))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(reverse("userauths:sign-in")))
        self.assertNotIn("_auth_user_id", self.client.session)
