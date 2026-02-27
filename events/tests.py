from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class EventAPITests(APITestCase):
    def test_create_event_success(self):
        url = reverse("event-list", kwargs={"version": "v1"})
        payload = {
            "name": "Tech Conference",
            "location": "Nairobi",
            "event_date": "2026-08-15",
            "slots": 100,
            "price": "49.99",
        }
        response = self.client.post(url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_event_invalid_slots(self):
        url = reverse("event-list", kwargs={"version": "v1"})
        payload = {
            "name": "Invalid Event",
            "location": "Mombasa",
            "event_date": "2026-08-16",
            "slots": -3,
            "price": "10.00",
        }
        response = self.client.post(url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("slots", response.data)
