from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Event, Registration

User = get_user_model()


class EventAPITests(APITestCase):
    def setUp(self):
        self.organizer = User.objects.create_user(
            email="organizer@example.com", password="password123"
        )
        self.other_user = User.objects.create_user(
            email="other@example.com", password="password123"
        )

        self.list_create_url = reverse("event-list-create")

        self.event_data = {
            "title": "Tech Conference 2026",
            "description": "Annual tech conference on AI and Django.",
            "date": (timezone.now() + timezone.timedelta(days=10)).isoformat(),
            "location": "Kyiv, Ukraine",
        }

        self.event = Event.objects.create(
            title="Existing Event",
            description="Existing description",
            date=timezone.now() + timezone.timedelta(days=5),
            location="Lviv, Ukraine",
            organizer=self.organizer,
        )
        self.detail_url = reverse("event-detail", kwargs={"pk": self.event.pk})

    def test_list_events_authenticated(self):
        self.client.force_authenticate(user=self.organizer)
        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_list_events_unauthenticated(self):
        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_event_success(self):
        self.client.force_authenticate(user=self.organizer)
        response = self.client.post(self.list_create_url, self.event_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], self.event_data["title"])
        self.assertEqual(response.data["organizer"]["email"], self.organizer.email)

    def test_retrieve_event_detail(self):
        self.client.force_authenticate(user=self.other_user)
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.event.title)

    def test_update_event_by_organizer(self):
        self.client.force_authenticate(user=self.organizer)
        update_payload = {
            "title": "Updated Title",
            "description": "Updated Description",
            "date": self.event.date.isoformat(),
            "location": "Odesa, Ukraine",
        }
        response = self.client.put(self.detail_url, update_payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.event.refresh_from_db()
        self.assertEqual(self.event.title, "Updated Title")

    def test_update_event_by_non_organizer_forbidden(self):
        self.client.force_authenticate(user=self.other_user)
        update_payload = {
            "title": "Hacked Title",
            "description": "Hacked Description",
            "date": self.event.date.isoformat(),
            "location": "Somewhere",
        }
        response = self.client.put(self.detail_url, update_payload)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_event_by_organizer(self):
        self.client.force_authenticate(user=self.organizer)
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Event.objects.filter(pk=self.event.pk).exists())

    def test_delete_event_by_non_organizer_forbidden(self):
        self.client.force_authenticate(user=self.other_user)
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Event.objects.filter(pk=self.event.pk).exists())


class RegistrationAPITests(APITestCase):
    def setUp(self):
        self.organizer = User.objects.create_user(
            email="organizer@example.com", password="password123"
        )
        self.participant = User.objects.create_user(
            email="participant@example.com", password="password123"
        )
        self.event = Event.objects.create(
            title="Python Meetup",
            description="Django REST Framework deep dive",
            date=timezone.now() + timezone.timedelta(days=3),
            location="Kharkiv, Ukraine",
            organizer=self.organizer,
        )
        self.register_url = reverse("event-register", kwargs={"pk": self.event.pk})

    def test_register_for_event_success(self):
        self.client.force_authenticate(user=self.participant)
        response = self.client.post(self.register_url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(
            Registration.objects.filter(user=self.participant, event=self.event).exists()
        )

    def test_register_for_event_duplicate_fails(self):
        self.client.force_authenticate(user=self.participant)
        self.client.post(self.register_url)
        response = self.client.post(self.register_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("already registered", response.data["detail"].lower())

    def test_cancel_registration_success(self):
        self.client.force_authenticate(user=self.participant)
        self.client.post(self.register_url)
        response = self.client.delete(self.register_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(
            Registration.objects.filter(user=self.participant, event=self.event).exists()
        )

    def test_cancel_registration_not_registered_fails(self):
        self.client.force_authenticate(user=self.participant)
        response = self.client.delete(self.register_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_register_unauthenticated_fails(self):
        response = self.client.post(self.register_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class EventFilterSearchAPITests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email="user1@example.com", password="password123")
        self.user2 = User.objects.create_user(email="user2@example.com", password="password123")
        self.list_url = reverse("event-list-create")

        self.now = timezone.now()

        self.event1 = Event.objects.create(
            title="Django World Conference",
            description="All about Python and Django REST framework",
            date=self.now + timezone.timedelta(days=1),
            location="Kyiv",
            organizer=self.user1,
        )

        self.event2 = Event.objects.create(
            title="React Frontend Meetup",
            description="Modern web application architecture",
            date=self.now + timezone.timedelta(days=10),
            location="Lviv",
            organizer=self.user2,
        )

    def test_filter_by_location(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(self.list_url, {"location": "Kyiv"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["id"], self.event1.id)

    def test_filter_by_organizer(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(self.list_url, {"organizer": self.user2.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["id"], self.event2.id)

    def test_search_by_keyword(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(self.list_url, {"search": "Django"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["id"], self.event1.id)

    def test_filter_by_date_range(self):
        self.client.force_authenticate(user=self.user1)
        date_from = (self.now + timezone.timedelta(days=5)).isoformat()
        response = self.client.get(self.list_url, {"date_from": date_from})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["id"], self.event2.id)
