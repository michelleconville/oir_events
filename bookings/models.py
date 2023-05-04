from django.db import models
from events.models import Event
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

TICKET_NUMBER = (("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"),)


class Booking(models.Model):
    """
    A model to create bookings, each user can book
    """
    user = models.ForeignKey(
        User, related_name="booking_owner", on_delete=models.CASCADE
    )
    title = models.ForeignKey(
         Event, related_name="event_name", on_delete=models.CASCADE
    )
    num_tickets = models.CharField(
        max_length=50, choices=TICKET_NUMBER, default="2"
        )
    booking_date = models.DateTimeField(auto_now_add=True)

    max_capacity = Event.objects.filter(max_capacity=True)

    class Meta:

        ordering = ['title']

    def __str__(self):
        return str(self.title)

    
