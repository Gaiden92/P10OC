# Generated by Django 5.0 on 2023-12-23 18:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="age",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(limit_value=15)]
            ),
        ),
    ]
