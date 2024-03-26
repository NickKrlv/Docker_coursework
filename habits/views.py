from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from habits.models import Habit
from habits.pagination import MyPagination
from habits.serializers import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = MyPagination
