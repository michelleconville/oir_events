from django.db import models
from events.models import Event
from django.contrib.auth.models import User

TICKET_NUMBER = (("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"),)


class Booking(models.Model):
    """
    A model to create bookings
    """
    user = models.ForeignKey(
        User, related_name="booking_owner", on_delete=models.CASCADE
    )
    event_name = models.ForeignKey(
        Event, related_name="event_name", on_delete=models.CASCADE
    )
    tour = models.ForeignKey(
        Event, related_name="tour", on_delete=models.CASCADE
    )
    ticket_number = models.CharField(
        max_length=50, choices=TICKET_NUMBER, default="2"
        )
    booking_date = models.DateField()

    class Meta:

        ordering = ['booking_date', 'ticket_number']

    def __str__(self):
        return str(self.pk)
