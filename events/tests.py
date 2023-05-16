from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Event


class EventTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username='testuser', password='testpassword', is_superuser=True
            )

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
        """Test Events model"""
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
        """Test Events list view"""
        url = reverse('events')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Event')

    def test_event_detail_view(self):
        """Test Event page view"""
        url = reverse('event_detail', kwargs={'pk': self.event.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.event.title)

    def test_add_event_view(self):
        """Test adding an events page view"""
        self.staff_user = User.objects.create_user(
            username='staffuser', password='testpassword', is_staff=True
            )
        self.client.login(username='staffuser', password='testpassword')
        url = reverse('add_event')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/add_event.html')

    def test_delete_event_view(self):
        """Test deleting an events page view"""
        self.staff_user = User.objects.create_user(
                username='staffuser', password='testpassword', is_staff=True
                )
        self.client.login(username='staffuser', password='testpassword')
        url = reverse('delete_event', kwargs={'pk': self.event.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/event_confirm_delete.html')

    def test_edit_event_view(self):
        """Test editing an events page view"""
        self.staff_user = User.objects.create_user(
                username='staffuser', password='testpassword', is_staff=True
                )
        self.client.login(username='staffuser', password='testpassword')
        url = reverse('edit_event', kwargs={'pk': self.event.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/edit_event.html')

    def test_add_event_view_end_user(self):
        """Test an end user can not access the add event form"""
        self.client.login(username='enduser', password='endpassword')
        url = reverse('add_event')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response)

    def test_edit_event_view_end_user(self):
        """Test an end user can not access the edit event form"""
        self.client.login(username='enduser', password='endpassword')
        url = reverse('edit_event', kwargs={'pk': self.event.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response)

    def test_delete_event_view_end_user(self):
        """Test an end user can not access the delete event page"""
        self.client.login(username='enduser', password='endpassword')
        url = reverse('delete_event', kwargs={'pk': self.event.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response)
