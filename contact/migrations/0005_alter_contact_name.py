# Generated by Django 3.2.18 on 2023-05-10 14:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contact", "0004_auto_20230502_1847"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="name",
            field=models.CharField(max_length=254, null=True),
        ),
    ]
