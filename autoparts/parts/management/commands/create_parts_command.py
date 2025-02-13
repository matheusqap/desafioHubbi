from django.core.management.base import BaseCommand
from autoparts.parts.tasks import create_periodic_tasks

class Command(BaseCommand):
    help = 'Create periodic tasks for AutoParts service.'

    def handle(self, *args, **kwargs):
        create_periodic_tasks()
        self.stdout.write(self.style.SUCCESS("Successfully created or updated periodic tasks."))