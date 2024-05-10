from django.test import TestCase
from userauth.models import User

class UserModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configuração dos dados de teste
        cls.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'phone_number': '123456789'
        }
        # Criar um usuário de exemplo
        cls.user = User.objects.create_user(**cls.user_data)

    def test_user_creation(self):
        # Testar se o usuário foi criado corretamente
        self.assertEqual(self.user.username, self.user_data['username'])
        self.assertEqual(self.user.email, self.user_data['email'])
        self.assertEqual(self.user.phone_number, self.user_data['phone_number'])

    def test_user_str_method(self):
        # Testar o método __str__() do modelo User
        self.assertEqual(str(self.user), self.user_data['username'])

    def test_default_user_permissions(self):
        # Testar se os privilégios de usuário padrão estão corretos
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)
