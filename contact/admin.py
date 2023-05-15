from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Class to view contact form details on admin panel
    """
    list_display = (
        "name",
        "email",
        "message",
        "posted_date",
    )
    list_filter = ("posted_date",)
