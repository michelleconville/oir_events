# Generated by Django 3.2.18 on 2023-05-10 17:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("bookings", "0012_booking_active"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="booking",
            name="active",
        ),
    ]
