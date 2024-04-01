from rest_framework import serializers
from habits.models import Habit
from habits.validators import EstimatedTimeValidator, HabitAndRewardValidator, PleasantHabitValidator, \
    LinkedHabitValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [EstimatedTimeValidator(field='estimated_time'),
                      HabitAndRewardValidator(habit='linked_habit', reward='reward'),
                      PleasantHabitValidator(pleasant='is_pleasant', reward='reward',
                                             linked_habit='linked_habit'),
                      LinkedHabitValidator(linked_habit='linked_habit'),]

