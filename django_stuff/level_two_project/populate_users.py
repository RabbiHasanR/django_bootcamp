import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','level_two_project.settings')

import django
django.setup()

##Fake pop script
from user_profile.models import User
from faker import Faker


fakergen=Faker()

def populate(N=5):
    for entry in range(N):

        #create the fake data for that entry
        fake_name=fakergen.name().split()
        fake_first_name=fake_name[0]
        fake_last_name=fake_name[1]
        fake_email=fakergen.email()

        #create the new webpage entry
        user=User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)[0]


if __name__=='__main__':
    print('Populating script!')
    populate(20)
    print('Populating complete!')
