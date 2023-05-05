from django.db import models
from events.models import Event
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django.core.exceptions import ValidationError


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
    num_tickets = models.PositiveIntegerField(default=1)
    booking_date = models.DateTimeField(auto_now_add=True)

    max_capacity = Event.objects.filter(max_capacity=True)

    class Meta:

        ordering = ['title']

    def __str__(self):
        return str(self.title)

    def clean(self):
        """
        Check if there are enough tickets available for the event
        """
        if self.num_tickets > self.title.max_capacity:
            raise ValidationError(
                f"Only {self.event.max_capacity} tickets available for this event"
            )
        return super().clean()

    def save(self, *args, **kwargs):
        """
        Check if the number of tickets is within the limit of 4 per booking
        """
        if self.pk is None and self.num_tickets > 4:
            raise ValidationError("Maximum of 4 tickets per booking")
        return super().save(*args, **kwargs)
