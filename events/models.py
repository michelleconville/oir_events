from django.db import models
from django.contrib.auth.models import User
from django import forms


from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField
from multiselectfield import MultiSelectField


# Choice Fields
GROUP_SIZE = ((20, "20"), (25, "25"), (30, "30"))

TOUR_TIMES = (
    ("10:00", "10:00"), ("10:30", "10:30"), ("11:00", "11:00"),
    ("11:30", "11:30"), ("12:00", "12:00"), ("12:30", "12:30"),
    ("12:30", "12:30"), ("14:00", "14:00"), ("14:30", "14:30"),
    ("15:00", "15:00"), ("15:30", "15:30"), ("16:00", "16:00"),
    ("16:30", "16:30"), ("17:00", "17:00"), ("17:30", "17:30"),
    ("18:00", "18:00"), ("18:30", "18:30"), ("19:00", "19:00"),
    ("19:30", "19:30"), ("20:00", "20:00"), ("20:30", "20:30"),
    ("21:00", "21:00"), ("21:30", "21:30"),
)


class Event(models.Model):
    """
    A model to create and manage events
    """

    user = models.ForeignKey(
        User, related_name="event_owner", on_delete=models.CASCADE
        )
    title = models.CharField(max_length=300, null=False, blank=False)
    summary = models.CharField(max_length=300, null=False, blank=False)
    description = RichTextField(max_length=10000, null=False, blank=False)
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="events/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    active = models.BooleanField(default=False)
    posted_date = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        User, related_name="event_likes", blank=True
        )
    max_capacity = models.SmallIntegerField(
        choices=GROUP_SIZE, default="20", db_index=True
    )
    event_date = models.DateField(blank=True, null=True)
    tour_times = MultiSelectField(
        max_length=300,
        choices=TOUR_TIMES, default="10:00"
    )

    booked_tickets = models.PositiveIntegerField(default=0)

    def current_bookings(self):
        return self.booking_set.count()

    class Meta:
        ordering = ["-posted_date"]

    def __str__(self):
        return str(self.title)

    def available_tickets(self):
        return self.max_capacity - self.booked_tickets
