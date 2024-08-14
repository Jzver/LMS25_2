from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email="jonnyzver78@gmail.com",
            is_staff=True,
            is_active=True,
            is_superuser=True,
        )
        user.set_password("Vladislava220913")
        user.save()