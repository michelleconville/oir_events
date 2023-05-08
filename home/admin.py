from django.contrib import admin
from .models import CarouselImage


@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = (
        "image",
        "caption"

    )
    list_filter = ("caption",)
