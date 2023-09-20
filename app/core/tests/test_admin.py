"""Tests for the Django admin modifications."""

# Django
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    """Test the Django admin modifications."""

    def setUp(self):
        """Set up the tests."""

        self.client = Client()

        self.admin_user = get_user_model().objects.create_superuser(
            email="superuser@example.org",
            password="testpass123",
        )
        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email="user@example.org",
            password="testpass123",
            name="Test user full name",
        )

    def test_users_list(self):
        """Test that users are listed on user page."""

        # Arrange
        url = reverse("admin:core_user_changelist")

        # Act
        res = self.client.get(url)

        # Assert
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self):
        """Test that the edit user page works."""

        # Arrange
        url = reverse("admin:core_user_change", args=[self.user.id])

        # Act
        res = self.client.get(url)

        # Assert
        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works."""

        # Arrange
        url = reverse("admin:core_user_add")

        # Act
        res = self.client.get(url)

        # Assert
        self.assertEqual(res.status_code, 200)
