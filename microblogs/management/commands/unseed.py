from django.core.management.base import BaseCommand, CommandError
from microblogs.models import User


class Command(BaseCommand):
    
    def handle(self, *args, **options):
        print("deleting all users excluding superusers.")
        User.objects.exclude(username = "admin").delete()
            
