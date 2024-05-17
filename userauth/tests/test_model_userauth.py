from django.test import TestCase

from userauth.models import User


class UserModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):

        cls.user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "phone_number": "123456789",
        }

        cls.user = User.objects.create_user(**cls.user_data)

    def test_user_creation(self):

        self.assertEqual(self.user.username, self.user_data["username"])
        self.assertEqual(self.user.email, self.user_data["email"])
        self.assertEqual(self.user.phone_number, self.user_data["phone_number"])

    def test_user_str_method(self):

        self.assertEqual(str(self.user), self.user_data["username"])

    def test_default_user_permissions(self):

        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)
