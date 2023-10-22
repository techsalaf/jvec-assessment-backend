

# contacts/tests/test_views.py

from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Contact

class ContactTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()

    def test_create_contact(self):
        self.client.force_authenticate(user=self.user)
        data = {'first_name': 'John', 'last_name': 'Doe', 'phone_number': '+1234567890'}
        response = self.client.post('/api/contacts/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Contact.objects.count(), 1)

    # Add more test cases for other views
