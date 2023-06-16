"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    """tests model"""
    def test_create_ueser_with_email(self):
        """Test creating user with an email"""
        email = 'abcdefs@example.com'
        password = "testpass"
        user = get_user_model().objects.create_user(email=email,password=password)
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))
    
    def test_new_user_email_normaliszed(self):
        """Tests email is normalized for new users"""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@EXAMPLE.COM', 'test4@example.com']
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)
    def test_new_user_without_email_error(self):
        """Raises error if user doesnot provide an email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", 'test123')
        
    def test_create_super_user(self):
        """Test creating superuser."""
        user = get_user_model().objects.create_superuser("super@example", "test123")
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)