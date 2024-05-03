from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from events.models import Event
from event_management.users.models import User
from rest_framework_simplejwt.tokens import AccessToken
from typing import Any
from datetime import datetime
class EventManagementTestCase(TestCase):
    def setUp(self) -> None:
        self.client: Any = APIClient()
        self.user: User = User.objects.create_user(email='test@example.com', password='testpassword')
        self.token: str = str(AccessToken.for_user(self.user))
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        self.event: Event = Event.objects.create(title='Test Event',date=datetime.now(), description='Test Description', owner=self.user)

    def test_get_event(self) -> None:
        url: str = reverse('apis:event-management', kwargs={'pk': self.event.pk})
        response: Any = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_event(self) -> None:
        url: str = reverse('apis:create-event')
        data: dict = {'title': 'New Event','date':'2024-02-02', 'location':'karachi,Pakistan','description': 'New Description'}
        response: Any = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_event(self) -> None:
        url: str = reverse('apis:event-management', kwargs={'pk': self.event.pk})
        data: dict = {'title': 'updated Event','date':'2024-01-05', 'location':'updated karachi,Pakistan',
                      'description': 'updated Description'}
        response: Any = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_event(self) -> None:
        url: str = reverse('apis:event-management', kwargs={'pk': self.event.pk})
        response: Any = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class AttendEventTestCase(TestCase):
    def setUp(self) -> None:
        self.client: Any = APIClient()
        self.user: User = User.objects.create_user(email='test@example.com', password='testpassword')
        self.user_02: User = User.objects.create_user(email='test02@example.com', password='testpassword')

        self.token: str = str(AccessToken.for_user(self.user))
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        self.event: Event = Event.objects.create(title='Test Event',date=datetime.now(), 
                                                 description='Test Description', owner=self.user_02)

    def test_attend_event(self) -> None:
        url: str = reverse('apis:attend-event', kwargs={'event_id': self.event.pk})
        response: Any = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_attend_event_already_attending(self) -> None:
        self.event.attendees.add(self.user)
        url: str = reverse('apis:attend-event', kwargs={'event_id': self.event.pk})
        response: Any = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_attend_event_owner(self) -> None:
        self.event.owner = self.user
        self.event.save()
        url: str = reverse('apis:attend-event', kwargs={'event_id': self.event.pk})
        response: Any = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
