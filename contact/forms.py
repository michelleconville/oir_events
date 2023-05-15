from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """Form for the contact page"""

    class Meta:
        model = Contact
        fields = [
            "name",
            "email",
            "message",
        ]

        widget = {
            "description": forms.Textarea(attrs={"rows": 10}),
        }
