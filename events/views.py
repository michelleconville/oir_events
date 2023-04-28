from django.views.generic import CreateView

from .models import Event
from .forms import EventForm


class AddEvent(CreateView):
    """ Add event view """
    template_name = 'events/add_event.html'
    model = Event
    form_class = EventForm
    success_url = '/events/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddEvent, self).form_valid(form)
