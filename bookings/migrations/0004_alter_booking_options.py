# Generated by Django 3.2.18 on 2023-05-03 15:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("bookings", "0003_ticket"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="booking",
            options={"ordering": ["user", "event_name"]},
        ),
    ]
