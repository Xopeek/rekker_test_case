from django.core.management.base import BaseCommand

from personal_feed.models import Achievement
from users.models import User


class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def handle(self, *args, **options):
        User.objects.create_user(
            username='user1',
            password='password1',
            first_name='John',
            last_name='Doe'
        )
        User.objects.create_user(
            username='user2',
            password='password2',
            first_name='Jane',
            last_name='Smith'
        )

        Achievement.objects.create(
            name='Впервые!',
            condition='Сделайте первую заметку'
        )
        Achievement.objects.create(
            name='Все работает!',
            condition='Получите первую ленту'
        )

        self.stdout.write(
            self.style.SUCCESS('Successfully populated the database')
        )
