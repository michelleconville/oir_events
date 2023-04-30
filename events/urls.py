from django.urls import path
from .views import AddEvent


urlpatterns = [
    path("add/", AddEvent.as_view(), name="add_event"),
    path("events/", Events.as_view(), name="events"),

]