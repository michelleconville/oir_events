from django.urls import path
from .views import (
    CreateBooking,
    UserBookings,
    StaffBookings,
    EditBooking,
    DeleteBooking,
)


urlpatterns = [
    path("add/", CreateBooking.as_view(), name="create_booking"),
    path("user_bookings/", UserBookings.as_view(), name="user_bookings"),
    path("staff_bookings/", StaffBookings.as_view(), name="staff_bookings"),
    path("bookings/<int:pk>/edit/", EditBooking.as_view(), name="edit_booking"),
    path("bookings/<int:pk>/delete/", DeleteBooking.as_view(), name="delete_booking"),
]
