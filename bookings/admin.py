from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "event_name",
        "ticket_number"
    )
    list_filter = ("event_name",)
