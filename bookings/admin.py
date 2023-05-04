from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "title",
        "num_tickets",
        "booking_date",
    )
    list_filter = ("user",)
