"""Tests for models."""

# Django
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful."""

        # Arrange
        email = "test@example.org"
        password = "testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        # Act
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized."""

        # Arrange
        sample_email = [
            ["test1@EXAMPLE.org", "test1@example.org"],
            ["Test2@Example.org", "Test2@example.org"],
            ["TEST3@EXAMPLE.ORG", "TEST3@example.org"],
            ["test4@example.ORG", "test4@example.org"],
        ]

        # Act
        for email, expected in sample_email:
            user = get_user_model().objects.create_user(email, "testpass123")

            # Assert
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test creating user without email raises error."""

        # Arrange
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "testpass123")

    def test_create_new_superuser(self):
        """Test creating a new superuser."""

        # Arrange
        user = get_user_model().objects.create_superuser(
            "test@example.org",
            "testpass123",
        )

        # Assert
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
