from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Event


class EventForm(forms.ModelForm):
    """Form to create a event"""

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
            "tour_times"
        ]

        description = forms.CharField(widget=RichTextWidget())

        widget = {
            "description": forms.Textarea(attrs={"rows": 10}),
            "event_date": forms.DateInput(attrs={"type": "date"}),
        }
