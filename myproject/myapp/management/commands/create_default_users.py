# myapp/management/commands/create_default_users.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create default users'

    def handle(self, *args, **kwargs):
        # Create a default admin user
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
            self.stdout.write(self.style.SUCCESS('Successfully created admin user'))

        # Create a default normal user
        if not User.objects.filter(username='user').exists():
            User.objects.create_user('user', 'user@example.com', '123default')
            self.stdout.write(self.style.SUCCESS('Successfully created default user'))
