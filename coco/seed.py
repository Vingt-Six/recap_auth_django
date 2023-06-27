from django_seed import Seed
from .models import *
from django.contrib.auth.hashers import make_password

def run():
    seeder = Seed.seeder()

    roles = [
        {'role': 'Admin'},
        {'role': 'Member'},
        {'role': 'Banned'},
    ]

    for item in roles:
        seeder.add_entity(Role, 1, item)
    
    print(seeder.execute())

    users = [
        {'username': 'admin', 'email': 'admin@admin.com', 'password': make_password('1234'), 'role': Role.objects.all()[0]},
        {'username': 'member', 'email': 'member@member.com', 'password': make_password('1234'), 'role': Role.objects.all()[1]},
        {'username': 'banned', 'email': 'banned@banned.com', 'password': make_password('1234'), 'role': Role.objects.all()[2]},
    ]

    for item in users:
        seeder.add_entity(User, 1, item)

    print(seeder.execute())