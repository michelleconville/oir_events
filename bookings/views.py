from django.views.generic import CreateView
from django.contrib import messages

from events.models import Event
from .models import Booking
from .forms import BookingForm


class CreateBooking(CreateView):
    """ # """
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
