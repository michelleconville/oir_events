from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "active",
        "event_date",
        "tour_times",
        "max_capacity",
        "booked_tickets",
        "image",
    )
    list_filter = ("title",)
