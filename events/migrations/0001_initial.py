# Generated by Django 3.2.18 on 2023-04-28 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import djrichtextfield.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=300)),
                ("summary", models.CharField(max_length=300)),
                ("description", djrichtextfield.models.RichTextField(max_length=10000)),
                (
                    "image",
                    django_resized.forms.ResizedImageField(
                        crop=None,
                        force_format="WEBP",
                        keep_meta=True,
                        quality=75,
                        scale=None,
                        size=[400, None],
                        upload_to="events/",
                    ),
                ),
                ("image_alt", models.CharField(max_length=100)),
                ("active", models.BooleanField(default=False)),
                ("posted_date", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="event_owner",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-posted_date"],
            },
        ),
    ]
