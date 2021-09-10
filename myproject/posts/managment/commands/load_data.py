import json
from django.core.management.base import BaseCommand
from posts.models import CustomUser


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        with open('posts/data/users.json', encoding='utf-8') as file:
            file_reader = file
            for row in file_reader:
                # do something with row data.
                id, name, username, email, phone, website = row
                CustomUser.objects.get_or_create(id=id, name=name, username=username, email=email, phone=phone, website=website)
                # print(name + ', ' + unit)