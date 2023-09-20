"""Test custom Django management commands."""

# Standard libraries
from unittest.mock import patch

# Django
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase

# Third-party libraries
from psycopg2 import OperationalError as Psycopg2OperationalError


@patch("core.management.commands.wait_for_db.Command.check")
class TestCommands(SimpleTestCase):
    """Test Commands class."""

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for database when database is available."""

        # Arrange
        patched_check.return_value = True

        # Act
        call_command("wait_for_db")

        # Assert
        patched_check.assert_called_once_with(databases=["default"])

    @patch("time.sleep")
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """
        Test waiting for database when database is available after some
        delay.
        """

        # Arrange
        patched_check.side_effect = [Psycopg2OperationalError] * 2 + \
                                    [OperationalError] * 3 + [True]

        # Act
        call_command("wait_for_db")

        # Assert
        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=["default"])
