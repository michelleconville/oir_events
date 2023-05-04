from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "summary",
        "image",
        "active",
        "event_date",
        "tour_times",
        "max_capacity"
    )
    list_filter = ("title",)
