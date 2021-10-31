from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from django.core.exceptions import ValidationError
from microblogs.models import User
import faker
class Command(BaseCommand):
    def __init__ (self):
        super().__init__()
        self.faker = Faker('en_GB')
        
    def combine(self,a,b):
        return a + "_" + b

    def handle(self,*args, **options):
        print("generating 100 random users.")
        self.__init__()
        try:
            for i in range(100):
                first_name = self.faker.unique.first_name()
                last_name = self.faker.unique.last_name()
                print("@" + self.combine(first_name,last_name))
                user = User.objects.create_user(
                username = "@" + self.combine(first_name,last_name),
                    first_name = first_name,
                    last_name = last_name,
                    email = self.faker.unique.email(),
                    password = self.faker.unique.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True),
                    bio = self.faker.unique.text())
                user.full_clean()
                user.save()
        except ValidationError:
            print(" The faker generates some illegal name, you should use Command \" python manage.py unseed \" and then seed again ")
        else:
            print(" successfully seeded ")

            
        
            

