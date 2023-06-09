from django.urls import path
from .views import AddEvent, Events, EventDetail, DeleteEvent, EditEvent


urlpatterns = [
    path("add/", AddEvent.as_view(), name="add_event"),
    path("", Events.as_view(), name="events"),
    path("<slug:pk>/", EventDetail.as_view(), name="event_detail"),
    path("delete/<slug:pk>/", DeleteEvent.as_view(), name="delete_event"),
    path("edit/<slug:pk>/", EditEvent.as_view(), name="edit_event"),
]
