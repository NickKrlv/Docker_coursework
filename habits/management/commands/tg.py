from django.core.management import BaseCommand

from habits.models import Habit
from users.services import MyBot


class Command(BaseCommand):
    def handle(self, *args, **options):
        bot = MyBot()
        habits = Habit.objects.filter(is_public=True)

        for habit in habits:
            bot.send_message(f"Вам следует совершить привычки: {habit.action} в {habit.time}")
