# Generated by Django 3.2.18 on 2023-04-30 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_tickets_per_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='tickets_per_session',
            field=models.SmallIntegerField(choices=[(20, '20'), (25, '25'), (30, '30')], db_index=True, default='20'),
        ),
    ]
