from django.db import models
from events.models import Event
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Booking(models.Model):
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

    def clean(self):
        available_tickets = self.title.available_tickets()
        if self.num_tickets > available_tickets:
            raise ValidationError(
                f"Only {available_tickets} tickets available for this event"
            )

        total_booked_tickets = self.title.booked_tickets + self.num_tickets
        if total_booked_tickets > self.title.max_capacity:
            raise ValidationError("Maximum capacity reached for this event")

        return super().clean()

    def save(self, *args, **kwargs):
        if self.pk is None and self.num_tickets > 4:
            raise ValidationError("Maximum of 4 tickets per booking")
        return super().save(*args, **kwargs)
