import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Создание фейковый данных для заполнения данных"

    def handle(self, *args, **kwargs):
        """ Метод обновления данных в базе новыми данными """

        shop_user = User.objects.create_superuser(username='admin', email='admin@mail.local')
        shop_user.set_password('testpass')
        shop_user.save()



# os.system('python manage.py createsuperuser')