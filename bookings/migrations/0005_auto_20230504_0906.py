# Generated by Django 3.2.18 on 2023-05-04 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_alter_booking_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='event_name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
        migrations.DeleteModel(
            name='Ticket',
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
