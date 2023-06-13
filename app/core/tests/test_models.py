"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    """tests model"""
    def test_create_ueser_with_email(self):
        """Test creating user with an email"""
        email = 'abc.defs@example.com'
        password = "testpass"
        user = get_user_model().objects.create_user(email=email,password=password)
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))