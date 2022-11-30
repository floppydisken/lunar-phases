from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Seeds the database with a user"

    def handle(self, *args, **kwargs):
        email = "vasilii@safeex.com"

        try:
            user = User.objects.get(email=email)
            print(f"{email} already exists. Skipping mock creation.")
            return
        except User.DoesNotExist:
            print(f"Creating user '{email}' with password '123456'")
            User.objects.create(username="vasilii@safeex.com",
                                password="123456", email="vasilii@safeex.com")
