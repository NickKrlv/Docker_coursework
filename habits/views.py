from django.db.models import Q
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from habits.models import Habit
from habits.pagination import MyPagination
from habits.permissions import IsOwner, IsStaff
from habits.serializers import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    pagination_class = MyPagination

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            return Habit.objects.all().order_by("id")
        else:
            return Habit.objects.filter(Q(user=self.request.user) | Q(is_public=True)).order_by("id")

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)
        else:
            raise ValueError(serializer.errors)

    def get_permissions(self):
        if self.action == "list":
            self.permission_classes = [IsAuthenticated]
        elif self.action == "retrieve":
            self.permission_classes = [IsAuthenticated]
        elif self.action == "create":
            self.permission_classes = [IsAuthenticated]
        elif self.action == "update" or self.action == "partial_update":
            self.permission_classes = [IsAuthenticated, IsOwner | IsStaff]
        elif self.action == "destroy":
            self.permission_classes = [IsAuthenticated, IsOwner | IsStaff]
        return super().get_permissions()
