from celery import shared_task
from .services import MyBot
from habits.models import Habit
from datetime import timedelta, datetime
import pytz


@shared_task
def notify():
    MSK = pytz.timezone('Europe/Moscow')
    my_bot = MyBot()
    messages = []
    habits = Habit.objects.all()
    time_from = datetime.now(MSK)
    time_till = time_from + timedelta(hours=1)
    for habit in habits:
        delta = timedelta(seconds=habit.estimated_time.second)
        started_time = habit.time
        current_time = started_time
        if current_time >= time_from:
            while time_till >= current_time:
                message = (f'Напоминание: я буду {habit.action} в {current_time.astimezone(MSK).isoformat()} в '
                           f'{habit.place}. На выполнение {habit.estimated_time} секунд.')
                messages.append(message)
                current_time += delta
    for msg in messages:
        my_bot.send_message(msg)
