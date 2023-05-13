from django.test import TestCase
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Event


class EventTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpassword', is_superuser=True)

        # Create an event for testing
        self.event = Event.objects.create(
            user=self.user,
            title='Test Event',
            summary='Test summary',
            description='Test description',
            image='path/to/test/image.jpg',
            image_alt='Test alt text',
            active=True,
            event_date='2023-05-15',
            max_capacity=20,
            tour_times='10:00',
            booked_tickets=0
        )

    def test_event_model(self):
        event = self.event
        self.assertEqual(event.title, 'Test Event')
        self.assertEqual(event.summary, 'Test summary')
        self.assertEqual(event.description, 'Test description')
        self.assertEqual(event.image, 'path/to/test/image.jpg')
        self.assertEqual(event.image_alt, 'Test alt text')
        self.assertTrue(event.active)
        self.assertEqual(str(event.event_date), '2023-05-15')
        self.assertEqual(event.max_capacity, 20)
        self.assertEqual(event.tour_times, '10:00')
        self.assertEqual(event.booked_tickets, 0)

    def test_event_list_view(self):
        url = reverse('events')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Event')

    def test_event_detail_view(self):
        url = reverse('add_event', kwargs={'pk': self.event.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.event.title)