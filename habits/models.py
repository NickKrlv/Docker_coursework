from django.contrib.auth import get_user_model
from django.db import models

NULLABLE = {'null': True, 'blank': True}

INTERVAL_CHOICES = [
    ('once_a_day', 'Один раз в день'),
    ('once_a_two_days', 'Один раз в два дня'),
    ('once_a_three_days', 'Один раз в три дня'),
    ('once_a_four_days', 'Один раз в четыре дня'),
    ('once_a_five_days', 'Один раз в пять дней'),
    ('once_a_six_days', 'Один раз в шесть дней'),
    ('once_a_week', 'Один раз в неделю'),
]


class Habit(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Пользователь')
    place = models.CharField(max_length=100, verbose_name='Место')
    time = models.DateTimeField(verbose_name='Время')
    action = models.TextField(verbose_name='Действие')
    pleasant = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    linked_habit = models.ForeignKey('self', on_delete=models.CASCADE, **NULLABLE, verbose_name='Связанная привычка')
    frequency = models.CharField(verbose_name='Частота', choices=INTERVAL_CHOICES, default='once_a_day')
    reward = models.CharField(max_length=100, verbose_name='Вознаграждение', **NULLABLE)
    estimated_time = models.TimeField(verbose_name='Время на выполнение', **NULLABLE)
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
