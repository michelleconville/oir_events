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
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        num_tickets = cleaned_data.get("num_tickets")

        if title and num_tickets:
            # Check if there are enough tickets available.
            if int(num_tickets) > title.available_tickets():
                raise forms.ValidationError(
                    f"Only {title.available_tickets()} tickets available"
                )

            # Check if the number of tickets is greater than 4.
            if int(num_tickets) > 4:
                raise forms.ValidationError("Maximum of 4 tickets per booking")

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Update queryset for 'title' field to only include active events
        self.fields['title'].queryset = Event.objects.filter(active=True)
