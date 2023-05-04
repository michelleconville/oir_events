from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "title",
        "ticket_number",
        "booking_date",
    )
    list_filter = ("user",)
