from django.views.generic import CreateView, ListView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Event
from .forms import EventForm


class Events(ListView):
    """View all events"""

    template_name = "events/events.html"
    model = Event
    context_object_name = "events"


class EventDetail(DetailView):
    """View a event"""

    template_name = "events/event_detail.html"
    model = Event
    context_object_name = "event"


class AddEvent(LoginRequiredMixin, CreateView):
    """Add event view"""

    template_name = "events/add_event.html"
    model = Event
    form_class = EventForm
    success_url = "/events/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddEvent, self).form_valid(form)
