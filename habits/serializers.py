from datetime import timedelta

from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'

    def validate(self, data):
        linked_habit = data.get('linked_habit')
        reward = data.get('reward')
        pleasant = data.get('pleasant')
        estimated_time = data.get('estimated_time')

        # Исключить одновременный выбор связанной привычки и указания вознаграждения
        if linked_habit and reward:
            raise serializers.ValidationError(
                _('Необходимо выбрать либо связанную привычку, либо указать вознаграждение, но не одновременно.'))

        # Время выполнения должно быть не больше 120 секунд
        if estimated_time and timedelta(hours=estimated_time.hour, minutes=estimated_time.minute,
                                        seconds=estimated_time.second).total_seconds() > 120:
            raise serializers.ValidationError(_('Время выполнения не может превышать 120 секунд.'))

        # Связанные привычки могут попадать только привычки с признаком приятной привычки
        if linked_habit and not linked_habit.pleasant:
            raise serializers.ValidationError(_('Связанная привычка должна быть приятной привычкой.'))

        # У приятной привычки не может быть вознаграждения или связанной привычки
        if pleasant and (reward or linked_habit):
            raise serializers.ValidationError(
                _('Приятная привычка не может иметь вознаграждения или связанных привычек.'))

        # Нельзя выполнять привычку реже, чем 1 раз в 7 дней - не понял, я же могу просто не добавлять варианты больше,
        # чем 1 раз в 7 дней

        return data
