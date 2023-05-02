from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """Form to create a event"""

    class Meta:
        model = Contact
        fields = '__all__'

        widget = {
            "description": forms.Textarea(attrs={"rows": 10}),
        }
