# Generated by Django 3.2.18 on 2023-05-08 18:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="carouselimage",
            name="cta_text",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]