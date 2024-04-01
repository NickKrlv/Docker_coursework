from datetime import timedelta
from django.utils.translation import gettext_lazy as _
from rest_framework.serializers import ValidationError
from habits.models import Habit


class EstimatedTimeValidator:
    """ Время выполнения должно быть не больше 120 секунд. """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        field_value = dict(value).get(self.field)
        if field_value and timedelta(hours=field_value.hour, minutes=field_value.minute,
                                        seconds=field_value.second).total_seconds() > 120:
            raise ValidationError(_('Время выполнения не может превышать 120 секунд.'))


class HabitAndRewardValidator:
    """ Исключить одновременный выбор связанной привычки и указания вознаграждения """

    def __init__(self, habit, reward):
        self.field_habit = habit
        self.field_reward = reward

    def __call__(self, value):
        habit = dict(value).get(self.field_habit)
        reward = dict(value).get(self.field_reward)
        if habit is not None and reward != '':
            raise ValidationError('Исключить одновременный выбор связанной привычки и указания вознаграждения')


class PleasantHabitValidator:
    """ У приятной привычки не может быть вознаграждения или связанной привычки """

    def __init__(self, pleasant, reward, linked_habit):
        self.field_pleasant = pleasant
        self.field_reward = reward
        self.field_linked_habit = linked_habit

    def __call__(self, value):
        pleasant = dict(value).get(self.field_pleasant)
        reward = dict(value).get(self.field_reward)
        linked_habit = dict(value).get(self.field_linked_habit)
        if pleasant and (reward != '' or linked_habit is not None):
            raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки')


class LinkedHabitValidator:
    """ В связанные привычки могут попадать только привычки с признаком приятной привычки """

    def __init__(self, linked_habit):
        self.field_linked_habit = linked_habit

    def __call__(self, value):
        linked_habit = value.get(self.field_linked_habit)
        if linked_habit and not linked_habit.pleasant:
            raise ValidationError(_('Связанная привычка должна быть приятной привычкой.'))
