from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Class to view bookings on admin panel
    """
    list_display = (
        "pk",
        "user",
        "title",
        "num_tickets",
        "booking_date",
    )
    list_filter = (
        "title",
        "booking_date",
    )
