# Generated by Django 3.2.18 on 2023-05-08 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_event_booked_tickets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='tour_times',
            field=models.CharField(choices=[('10:00', '10:00'), ('10:30', '10:30'), ('11:00', '11:00'), ('11:30', '11:30'), ('12:00', '12:00'), ('12:30', '12:30'), ('12:30', '12:30'), ('14:00', '14:00'), ('14:30', '14:30'), ('15:00', '15:00'), ('15:30', '15:30'), ('16:00', '16:00'), ('16:30', '16:30'), ('17:00', '17:00'), ('17:30', '17:30'), ('18:00', '18:00'), ('18:30', '18:30'), ('19:00', '19:00'), ('19:30', '19:30'), ('20:00', '20:00'), ('20:30', '20:30'), ('21:00', '21:00'), ('21:30', '21:30')], default='10:00', max_length=50),
        ),
    ]
