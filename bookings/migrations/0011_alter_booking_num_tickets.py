# Generated by Django 3.2.18 on 2023-05-05 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0010_auto_20230504_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='num_tickets',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
