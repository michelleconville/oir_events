# Generated by Django 3.2.18 on 2023-05-07 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_rename_tickets_per_session_event_max_capacity'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='booked_tickets',
            field=models.PositiveIntegerField(default=0),
        ),
    ]