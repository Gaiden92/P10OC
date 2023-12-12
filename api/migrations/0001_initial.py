# Generated by Django 5.0 on 2023-12-09 14:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("name", models.CharField(max_length=65)),
                ("description", models.TextField(max_length=255)),
                (
                    "project_type",
                    models.CharField(
                        choices=[
                            ("backend", "backend"),
                            ("frontend", "frontend"),
                            ("ios", "IOS"),
                            ("android", "Android"),
                        ],
                        max_length=65,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                ("created_time", models.DateTimeField(auto_now_add=True)),
                ("username", models.CharField(max_length=65)),
                (
                    "age",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(15),
                            django.core.validators.MaxValueValidator(80),
                        ]
                    ),
                ),
                ("can_be_contacted", models.BooleanField(default=False)),
                ("can_data_be_shared", models.BooleanField(default=False)),
            ],
        ),
    ]