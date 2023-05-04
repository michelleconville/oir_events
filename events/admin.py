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
        "tickets_per_session",
        "tour_times",
    )
    list_filter = ("title",)
