from django.utils import timezone

from django.core.management.base import BaseCommand
from django.db import connection

from habits.models import Habit
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute(
                "TRUNCATE TABLE users_user, habits_habit RESTART IDENTITY CASCADE")
        admin = User.objects.create(email='admin@sky.pro', password='admin', is_superuser=True, is_staff=True)
        user1 = User.objects.create(email='user1@sky.pro')
        user2 = User.objects.create(email='user2@sky.pro')
        admin.set_password('admin')
        admin.save()
        user1.set_password('user1')
        user1.save()
        user2.set_password('user2')
        user2.save()

        habit_1 = Habit.objects.create(
            user=user1,
            place='Дом',
            time=timezone.make_aware(timezone.datetime(2025, 1, 1, 0, 0, 0)),  # Используйте timezone.make_aware
            action='Покушание',
            pleasant=True,
            reward='Покушал и кайфуешь',
            frequency='once_a_day',
            estimated_time='00:02:00',
            is_public=True)
        habit_1.save()

        habit_2 = Habit.objects.create(
            user=user1,
            place='Магазин',
            time=timezone.make_aware(timezone.datetime(2025, 1, 1, 0, 0, 0)),  # Используйте timezone.make_aware
            action='Покупка продуктов',
            pleasant=False,
            frequency='once_a_week',
            linked_habit=habit_1,
            estimated_time='00:02:00',
            is_public=True)
        habit_2.save()

        habit_3 = Habit.objects.create(
            user=user2,
            place='Дом',
            time=timezone.make_aware(timezone.datetime(2025, 1, 1, 0, 0, 0)),  # Используйте timezone.make_aware
            action='Сделать сальтушку',
            pleasant=False,
            frequency='once_a_day',
            reward='Повышение ЧСВ',
            estimated_time='00:02:00',
            is_public=False)
        habit_3.save()

        self.stdout.write(self.style.SUCCESS('Вы успешно загрузили данные, как успешный человек.'))
