# Generated by Django 3.2.18 on 2023-05-04 15:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bookings", "0006_booking"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="booking_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
