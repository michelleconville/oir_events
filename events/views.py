from django.views.generic import (
    CreateView, ListView,
    DetailView, DeleteView,
    UpdateView
)

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages

from .models import Event
from .forms import EventForm


class Events(ListView):
    """View all events"""
    template_name = "events/events.html"
    model = Event
    context_object_name = "events"

    def get_queryset(self):
        return Event.objects.filter(active=True)


class EventDetail(DetailView):
    """View an event"""
    template_name = "events/event_detail.html"
    model = Event
    context_object_name = "event"

    # def get_queryset(self):
    #     return Event.objects.filter(active=True)

    def get_queryset(self):
        return Event.objects.all()

    def test_func(self):
        return self.request.user.is_staff

    def get_queryset(self):
        return Event.objects.annotate(num_likes=models.Count('likes'))


class AddEvent(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """AddEvent view to create an event if the user is staff"""
    template_name = "events/add_event.html"
    model = Event
    form_class = EventForm
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
            'Event successfully created'
        )
        return super(AddEvent, self).form_valid(form)


class EditEvent(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit an Event"""
    template_name = "events/add_event.html"
    model = Event
    form_class = EventForm
    success_url = "/events/"

    def form_valid(self, form):
        messages.success(
            self.request,
            'Event successfully updated'
        )
        return super(EditEvent, self).form_valid(form)

    def test_func(self):
        return self.request.user.is_staff


class DeleteEvent(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete an Event"""
    model = Event
    success_url = "/events/"

    def test_func(self):
        if self.request.user.is_staff:
            return True
        else:
            return False

    def form_valid(self, form):
        messages.success(
            self.request,
            'Event successfully deleted'
        )
        return super(DeleteEvent, self).form_valid(form)
