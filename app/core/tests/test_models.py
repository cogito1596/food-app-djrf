from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = "jakeops1999@gmail.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        sample_email = [
            ["test4@EXAMPLE.COM", "test4@example.com"],
            ["Test2@example.com", "Test2@example.com"],
            ["test3@example.COM", "test3@example.com"],
        ]
        for email, expected_email in sample_email:
            user = get_user_model().objects.create_user(email=email, password="test123")
            self.assertEqual(user.email, expected_email)

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_new_superuser(self):
        email = "jakeops1999@gmail.com"
        password = "testpass123"
        user = get_user_model().objects.create_superuser(email=email, password=password)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
