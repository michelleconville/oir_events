from django.urls import path
from .views import CreateBooking


urlpatterns = [
    path("add/", CreateBooking.as_view(), name="add_booking"),

]
