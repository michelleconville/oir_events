from django.urls import path
from .views import AddEvent, Events, EventDetail


urlpatterns = [
    path("add/", AddEvent.as_view(), name="add_event"),
    path("events/", Events.as_view(), name="events"),
    path("<slug:pk>/", EventDetail.as_view(), name="event_detail"),
]
