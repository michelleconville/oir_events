from django.db import models
from cloudinary.models import CloudinaryField
import cloudinary


class CarouselImage(models.Model):
    image = cloudinary.models.CloudinaryField('image')
    caption = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    cta_text = models.CharField(max_length=255, blank=True)
    cta_url = models.URLField(max_length=255, blank=True)

    def __str__(self):
        return self.caption
