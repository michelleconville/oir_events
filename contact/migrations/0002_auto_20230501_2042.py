# Generated by Django 3.2.18 on 2023-05-01 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=254, null=True)),
                ('last_name', models.CharField(blank=True, max_length=254, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=16, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('posted_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ContactForm',
        ),
    ]
