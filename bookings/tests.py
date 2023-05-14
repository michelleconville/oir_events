from django.test import TestCase
from django.contrib.auth.models import User
from events.models import Event
from .models import Booking


class TestViews(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username='testuser', password='testpassword', is_superuser=True
            )

        self.user.is_staff = True
        self.user.save()

        logged_in = self.client.login(
            username='testuser', password='testpassword'
            )
        self.assertTrue(logged_in)

        # Create an event for testing
        event = Event.objects.create(
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

        # Create an booking for testing
        booking = Booking.objects.create(
            user=self.user, title=event, num_tickets=2
            )

    def test_booking_list(self):
        """ Test Manage Bookings """
        response = self.client.get('/bookings/user_bookings/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/user_bookings.html')

    def test_booking_staff_list(self):
        """ Test Staff Manage Bookings """
        response = self.client.get('/bookings/staff_bookings/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/staff_bookings.html')

    def test_booking_overview_staff(self):
        """ Test Staff Booking overview """
        response = self.client.get('/bookings/booking_overview/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/booking_overview.html')

    def test_booking_overview_end_user(self):
        """Test End User Booking overview"""
        # Create an end user for testing
        end_user = User.objects.create_user(
            username='enduser', password='endpassword'
        )

        logged_in = self.client.login(
            username='enduser', password='endpassword'
            )
        self.assertTrue(logged_in)

        # Attempt to access the booking overview
        response = self.client.get('/bookings/booking_overview/')
        self.assertEqual(response.status_code, 403)
