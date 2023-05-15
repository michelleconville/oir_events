from django.db import models
from events.models import Event
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Booking(models.Model):
    """
    Model to create a booking
    """
    user = models.ForeignKey(
        User, related_name="booking_owner", on_delete=models.CASCADE
    )
    title = models.ForeignKey(
        Event, related_name="event_name", on_delete=models.CASCADE
    )
    num_tickets = models.PositiveIntegerField(default=1)
    booking_date = models.DateTimeField(auto_now_add=True)

    def max_capacity(self):
        return self.title.max_capacity

    def event_date(self):
        return self.title.event_date

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return str(self.title)
