from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from users.models import User


class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'email': 'test@example.com',
            'password': 'password123',
        }

    def test_create_user(self):
        response = self.client.post(reverse('users:user-list'), self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, 'test@example.com')

    def test_update_user(self):
        # Создаем пользователя
        response = self.client.post(reverse('users:user-list'), self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Получаем его ID
        user_id = response.data['id']

        # Обновляем данные пользователя
        update_data = {
            'password': 'newpassword123'
        }
        response = self.client.put(reverse('users:user-detail', kwargs={'pk': user_id}), update_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get(id=user_id).password, 'newpassword123')

