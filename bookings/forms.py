from django import forms
from django.core.exceptions import ValidationError

from .models import Booking
from events.models import Event


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            "title",
            "num_tickets",
        ]

        labels = {
            'title': 'Select an event ',
            'num_tickets': 'Number of tickets ',

        }
        

    def clean(self):
        """
        Check if there are enough tickets available for the event.
        """
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        num_tickets = cleaned_data.get("num_tickets")

        if title and num_tickets:
            # Check if there are enough tickets available.
            if int(num_tickets) > title.max_capacity - title.booked_tickets:
                raise forms.ValidationError(
                    f"Only {title.max_capacity - title.booked_tickets} tickets available for this event"
                )

            # Check if the number of tickets is greater than 4.
            if int(num_tickets) > 4:
                raise forms.ValidationError("Maximum of 4 tickets per booking")

        return cleaned_data
