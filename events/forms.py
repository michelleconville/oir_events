from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Event


class EventForm(forms.ModelForm):
    """ Form to create a event """
    class Meta:
        model = Event
        fields = ['title', 'summary', 'description', 'image', 'image_alt', 'active']

        description = forms.CharField(widget=RichTextWidget())

        widget = {
            "description": forms.Textarea(attrs={"rows": 10}),
        }
