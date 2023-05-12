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
            "title": "Event title",
            "summary": "Short description",
            "event_date": "Date of event",
            "max_capacity": "Tour size",
            "description": "Description of event",
            "image": "image",
            "image_alt": "Alt text",
            "tour_times": "Tour time",
            "active": "Publish event (Optional)",
        }

        widgets = {
            "description": RichTextWidget(),
            "event_date": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_description(self):
        description = self.cleaned_data.get("description")

        if not description:
            raise forms.ValidationError("Description is required.")

        return description

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        summary = cleaned_data.get("summary")
        event_date = cleaned_data.get("event_date")
        max_capacity = cleaned_data.get("max_capacity")

        if not title:
            self.add_error("title", "Title is required.")
        if not summary:
            self.add_error("summary", "Summary is required.")
        if not event_date:
            self.add_error("event_date", "Event date is required.")
        if not max_capacity:
            self.add_error("max_capacity", "Max capacity is required.")

        return cleaned_data
