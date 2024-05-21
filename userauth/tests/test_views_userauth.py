from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse

from userauth.models import User


class UserAuthViewsTest(TestCase):
    def setUp(self):
        self.user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpassword",
        }
        User = get_user_model()
        self.user = User.objects.create_user(**self.user_data)

    def test_register_view(self):
        response = self.client.get(reverse("userauths:sign-up"))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse("userauths:sign-up"), self.user_data)
        self.assertEqual(
            response.status_code, 200
        )  # Redirects after successful registration
        self.assertTrue(User.objects.filter(email=self.user_data["email"]).exists())

    def test_login_view(self):
        response = self.client.get(reverse("userauths:sign-in"))
        self.assertEqual(response.status_code, 200)

        # Test logging in with correct credentials
        response = self.client.post(
            reverse("userauths:sign-in"),
            {"email": "test@example.com", "password": "testpassword"},
        )
        self.assertEqual(response.status_code, 302)  # Redirects after successful login

        # Check if user is authenticated
        self.assertTrue(
            self.client.session["_auth_user_id"]
        )  # User should be authenticated

        # Redirects to the expected URL
        self.assertRedirects(response, reverse("pets:index"))

        # Test logging in with incorrect credentials
        response = self.client.post(
            reverse("userauths:sign-in"),
            {"email": "test@example.com", "password": "wrongpassword"},
        )
        self.assertEqual(
            response.status_code, 302
        )  # Redirects after unsuccessful login

    def test_logout_view(self):
        # Log in the user first
        self.client.login(email=self.user.email, password=self.user_data["password"])

        # Make a GET request to the logout URL
        response = self.client.get(reverse("userauths:sign-out"))

        # Check if the response is a redirect
        self.assertEqual(response.status_code, 302)  # Redirects after logout

        # Check if the redirection is to "userauths:sign-in"
        self.assertEqual(response.url, reverse("userauths:sign-in"))

        # Check if the user is not authenticated after logout
        self.assertFalse("_auth_user_id" in self.client.session)

        # Check if the success message is displayed
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "You have been logged out.")
