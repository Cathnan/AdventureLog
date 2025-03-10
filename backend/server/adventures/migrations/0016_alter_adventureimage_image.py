# Generated by Django 5.0.8 on 2025-01-01 21:40

import adventures.models
import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adventures', '0015_transportation_destination_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adventureimage',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=75, scale=None, size=[1920, 1080], upload_to=adventures.models.PathAndRename('images/')),
        ),
    ]
