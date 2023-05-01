# Generated by Django 3.2.18 on 2023-05-01 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=254, null=True)),
                ('last_name', models.CharField(blank=True, max_length=254, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=16, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
    ]