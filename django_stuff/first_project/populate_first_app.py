import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

##Fake pop script
import random
from first_app.models import Topic,WebPage,AccessRecord
from faker import Faker


fakergen=Faker()
topics=['Search','Social','Marketplace,News','Games']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):

        #get the topic for the entry
        top=add_topic()

        #create the fake data for that entry
        fake_name=fakergen.company()
        fake_url=fakergen.url()
        fake_date=fakergen.date()

        #create the new webpage entry
        webpage=WebPage.objects.get_or_create(topic=top,name=fake_name,url=fake_url)[0]

        #create the new AccessRecord
        acc_rec=AccessRecord.objects.get_or_create(name=webpage,date=fake_date)[0]


if __name__=='__main__':
    print('Populating script!')
    populate(20)
    print('Populating complete!')
