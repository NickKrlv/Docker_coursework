from django.contrib import admin
from .models import Habit
from users.models import User


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'place', 'time', 'action', 'frequency', 'reward', 'is_public')
    list_filter = ('user', 'frequency', 'is_public')
    search_fields = ('user__email', 'place', 'action', 'reward')
    list_editable = ('is_public', 'frequency')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_superuser', 'is_staff', 'is_active')
