from django.contrib import admin
from .models import CarouselImage


@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    """
    Class to view Carorsel images on admin panel
    """
    list_display = ("image", "caption", "cta_text", "cta_url", "description")
    list_filter = ("caption",)
