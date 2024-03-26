from .views import HabitViewSet
from rest_framework.routers import DefaultRouter

app_name = 'habits'

router = DefaultRouter()
router.register('habits', HabitViewSet, basename='habits')

urlpatterns = router.urls
