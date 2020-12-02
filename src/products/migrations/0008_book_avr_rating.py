# Generated by Django 3.1.2 on 2020-11-30 21:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20201102_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='avr_rating',
            field=models.SmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
            preserve_default=False,
        ),
    ]