# Generated by Django 3.2.18 on 2023-05-13 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_remove_event_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(null=True),
        ),
    ]