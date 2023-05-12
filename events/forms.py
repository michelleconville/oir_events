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
            "active",
            "tour_times",
        ]
        widgets = {
            "description": RichTextWidget(),
            "event_date": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
