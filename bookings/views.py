from django.views.generic import CreateView, ListView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render

from events.models import Event
from .models import Booking
from .forms import BookingForm


class CreateBooking(CreateView):
    """
    A view to create a new booking
    """
    template_name = "bookings/add_booking.html"
    model = Booking
    form_class = BookingForm
    success_url = "/events/"

    def form_valid(self, form):
        form.instance.user = self.request.user

        messages.success(
            self.request,
            'Booking successfully created'
        )
        return super(CreateBooking, self).form_valid(form)


class UserBookings(LoginRequiredMixin, ListView):
    """
    A view to display a list of bookings made by the user
    """
    template_name = "bookings/user_bookings.html"
    context_object_name = "bookings"

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


class StaffBookings(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """
    A view to display a list of all bookings
    """
    template_name = "bookings/staff_bookings.html"
    context_object_name = "bookings"
    model = Booking

    def test_func(self):
        return self.request.user.is_staff
