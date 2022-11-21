# Generated by Django 4.1.2 on 2022-11-10 19:41

import datetime

import django.core.serializers.json
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("records", "0002_movie"),
    ]

    operations = [
        migrations.CreateModel(
            name="Record",
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
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "reported_timestamp",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "time_to_live",
                    models.DurationField(default=datetime.timedelta(days=90)),
                ),
                ("is_recent", models.BooleanField(default=True)),
                ("is_trusted", models.BooleanField(default=False)),
                ("is_verified", models.BooleanField(default=False)),
                ("comment", models.TextField(max_length=256)),
                (
                    "type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("data_point", "Data Point"),
                            ("medical_report", "Medical Report"),
                            ("lab_result", "Lab Result"),
                            ("vax_card", "Vaccination Card"),
                            ("webscraper", "Webscraper"),
                            ("other", "Other"),
                        ],
                        default="",
                        max_length=144,
                    ),
                ),
                (
                    "raw_data",
                    models.JSONField(
                        default='{"key_1": "Value 1","next_value": "Next Value"}',
                        encoder=django.core.serializers.json.DjangoJSONEncoder,
                    ),
                ),
            ],
            options={
                "verbose_name": "record",
                "verbose_name_plural": "records",
                "ordering": ["updated_date"],
            },
        ),
    ]
