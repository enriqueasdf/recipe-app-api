""" Django command to wait for database to be available."""

# Standard libraries
import time

# Django
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError

# Third-party libraries
from psycopg2 import OperationalError as Psycopg2OperationalError


class Command(BaseCommand):
    """Command class."""

    def handle(self, *args, **options):
        """Handle the command."""
        self.stdout.write("Waiting for database...")
        database_is_available = False

        while not database_is_available:
            try:
                self.check(databases=["default"])
                database_is_available = True
            except (Psycopg2OperationalError, OperationalError):
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)
