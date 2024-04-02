from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from .models import Habit
from .serializers import HabitSerializer


class HabitViewTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(email='testuser@test.ru', password='12345')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(user=self.user, place='Home', time='2024-04-01T12:00:00Z',
                                          action='Test action', pleasant=False)

    def test_public_habit_list(self):
        response = self.client.get('/public_habits/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_create_habit(self):
        data = {'user': self.user.id, 'place': 'Office', 'time': '2024-04-02T09:00:00Z',
                'action': 'Another test action', 'pleasant': False}
        response = self.client.post('/habits/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 2)

    def test_update_habit(self):
        data = {'action': 'Updated action'}
        response = self.client.patch(f'/habits/{self.habit.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['action'], 'Updated action')

    def test_delete_habit(self):
        response = self.client.delete(f'/habits/{self.habit.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.count(), 0)


class HabitSerializerTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(email='testuser@test.ru', password='12345')
        self.habit_data = {'user': self.user.id, 'place': 'Home', 'time': '2024-04-01T12:00:00Z',
                           'action': 'Test action', 'pleasant': False}
        self.serializer = HabitSerializer(data=self.habit_data)

    def test_habit_serializer_valid(self):
        self.assertTrue(self.serializer.is_valid())

    def test_habit_serializer_invalid(self):
        habit_data_invalid = {'user': self.user.id, 'place': 'Home', 'time': '2024-04-01T12:00:00Z',
                              'action': '', 'pleasant': False}  # Action field is empty
        serializer = HabitSerializer(data=habit_data_invalid)
        self.assertFalse(serializer.is_valid())
        self.assertIn('action', serializer.errors)

    def test_habit_serializer_create(self):
        if self.serializer.is_valid():
            self.serializer.save()
        self.assertEqual(Habit.objects.count(), 1)
        self.assertEqual(Habit.objects.get().action, 'Test action')
