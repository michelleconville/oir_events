from django.views.generic import CreateView

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)

from django.contrib import messages

from .models import Booking


class CreateBooking(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """ # """
    template_name = "bookings/add_booking.html"
    model = Booking
    success_url = "/events/"

    def test_func(self):
        if self.request.user.is_staff:
            return True
        else:
            return False

    def form_valid(self, form):
        form.instance.user = self.request.user

        messages.success(
            self.request,
            'Booking successfully created'
        )
        return super(CreateBooking, self).form_valid(form)
