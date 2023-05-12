from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Event


class EventForm(forms.ModelForm):
    """Form to create an event"""

    class Meta:
        model = Event
        fields = [
            "title",
            "summary",
            "event_date",
            "max_capacity",
            "description",
            "image",
            "image_alt",
            "tour_times",
            "active",
        ]

        labels = {
            'title': 'Select an event ',
            "summary": "Short description",
            "event_date": "Date of event",
            "max_capacity": "Tour size",
            "description": "Description of event",
            "image": "image",
            "image_alt": "Alt text",
            "tour_times": "Tour time",
            "active": "Publish event (Optional)"
        }

        widgets = {
            "description": RichTextWidget(),
            "event_date": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
