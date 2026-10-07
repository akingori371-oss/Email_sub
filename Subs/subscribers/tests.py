from django.test import TestCase

from .models import Subscriber


class SubscriberViewTests(TestCase):
    def test_subscribe_page_loads(self):
        response = self.client.get('/subscribe/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Subscribe to Our Newsletter')

    def test_duplicate_email_is_rejected(self):
        Subscriber.objects.create(email='user@example.com')

        response = self.client.post('/subscribe/', {'email': 'user@example.com'})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'already subscribed')
        self.assertEqual(Subscriber.objects.filter(email='user@example.com').count(), 1)
