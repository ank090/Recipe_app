"""
Django command to wait for the database to be available.
"""
from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as Psycopg2OpError
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError

class Command(BaseCommand):
    """ Django command to wait for the database."""
    def handle(self,*args,**options):
        self.stdout.write("waiting for database...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError) as e:

                self.stdout.write(str(e)+"Database unavailable, waiting for 1 second...")
                time.sleep(1)
        
        self.stdout.write(self.style.SUCCESS('Connection With Database Established!'))