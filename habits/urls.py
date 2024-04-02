from django.urls import path

from .views import HabitViewSet, PublicHabitListAPIView
from rest_framework.routers import DefaultRouter

app_name = 'habits'

router = DefaultRouter()
router.register('habits', HabitViewSet, basename='habits')

urlpatterns = [path('public_habits/', PublicHabitListAPIView.as_view(), name='public-list'),
               ] + router.urls
