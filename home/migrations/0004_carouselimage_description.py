# Generated by Django 3.2.18 on 2023-05-08 19:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0003_carouselimage_cta_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="carouselimage",
            name="description",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]