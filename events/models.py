from django.db import models
from django.contrib.auth.models import User

from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField

# Choice Fields
GROUP_SIZE = ((20, "20"), (25, "25"), (30, "30"))


class Event(models.Model):
    """
    A model to create and manage events
    """
    user = models.ForeignKey(User, related_name='event_owner', on_delete=models.CASCADE)
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
    likes = models.ManyToManyField(User, related_name='event_likes', blank=True)
    tickets_per_session = models.SmallIntegerField(choices=GROUP_SIZE, default="20", db_index=True)

    class Meta:
        ordering = ["-posted_date"]

    def __str__(self):
        return str(self.title)
