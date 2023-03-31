from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UsersManagersTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(email="rod@example.com", password="testPass123")
        self.assertEqual(user.email,"rod@example.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="Foo")
    
    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(email="clark@dailyplanet.com", password="TestPass123")
        self.assertEqual(admin_user.email, "clark@dailyplanet.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        
        try:
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email="super@user.com",password="Foo",
                is_superuser=False)