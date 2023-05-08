from django.db import models
from cloudinary.models import CloudinaryField
import cloudinary


class CarouselImage(models.Model):
    image = cloudinary.models.CloudinaryField('image')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.caption
