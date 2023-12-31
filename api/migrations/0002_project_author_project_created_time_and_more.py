# Generated by Django 5.0 on 2023-12-09 15:58

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="author",
            field=models.ForeignKey(
                default=0, on_delete=django.db.models.deletion.CASCADE, to="api.user"
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="created_time",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="user",
            name="created_time",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
