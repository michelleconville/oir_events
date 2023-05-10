from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy

from events.models import Event
from .models import Booking
from .forms import BookingForm


class CreateBooking(LoginRequiredMixin, CreateView):
    """
    A view to create a new booking
    """
    template_name = "bookings/add_booking.html"
    model = Booking
    form_class = BookingForm
    success_url = "/events/"

    def form_valid(self, form):
        form.instance.user = self.request.user

        event = form.cleaned_data['title']
        num_tickets = form.cleaned_data['num_tickets']

        if num_tickets > event.available_tickets() or num_tickets + event.booked_tickets > event.max_capacity:
            messages.error(self.request, "Maximum capacity reached for this event")
            return redirect('/events/add_booking.html')

        get_event = Event.objects.get(title=event)
        get_event.booked_tickets = get_event.booked_tickets + num_tickets
        get_event.save()

        messages.success(self.request, "Booking successfully created")
        return super().form_valid(form)


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


class EditBooking(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    A view to edit a booking
    """

    template_name = "bookings/edit_booking.html"
    model = Booking
    form_class = BookingForm
    success_url = reverse_lazy("staff_bookings")

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        old_booking = self.get_object()
        new_booking = form.save(commit=False)

        num_tickets_diff = new_booking.num_tickets - old_booking.num_tickets

        if num_tickets_diff != 0:
            event = new_booking.title

            event.booked_tickets += num_tickets_diff
            event.save()

        messages.success(self.request, "Booking successfully updated")
        return super().form_valid(form)


class DeleteBooking(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a Booking"""

    model = Booking
    success_url = "/events/"

    def test_func(self):
        return self.request.user.is_authenticated

    def delete(self, request, *args, **kwargs):
        booking = self.get_object()
        event = booking.title
        event.booked_tickets -= booking.num_tickets
        event.save()

        messages.success(self.request, "Booking successfully deleted")
        return super().delete(request, *args, **kwargs)
