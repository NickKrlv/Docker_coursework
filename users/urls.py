from django.urls import path

from .views import UserViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'users'

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
                  path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
                  path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
              ] + router.urls
