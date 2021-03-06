from faker import Faker
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

## Fake pop ProDescription
import random

from appTwo.models import User

fakegen = Faker()

def populate(N):

    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        # New entry
        user = User.objects.get_or_create(first_name=fake_first_name,
                                          last_name=fake_last_name,
                                          email=fake_email)[0]

if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete!")
