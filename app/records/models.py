from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.utils import timezone

RECORD_TYPES = [
    ("data_point", "Data Point"),
    ("medical_report", "Medical Report"),
    ("lab_result", "Lab Result"),
    ("vax_card", "Vaccination Card"),
    ("webscraper", "Webscraper"),
    ("other", "Other"),
]


class CustomUser(AbstractUser):
    pass


class Movie(models.Model):
    """
    Example model (models.Model not Record)
    """

    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


class Record(models.Model):
    """
    Base model for any document to be shared.

    type is chosen from the tuple RECORD_TYPES.

    created_date is always the current time in default timezone (not UTC)

    reported_timestamp using django.utils.timezone is timezone aware datetime
    object stored as UTC in the datase but tz-aware to users.
    https://docs.djangoproject.com/en/4.1/topics/i18n/timezones/#naive-and-aware-datetime-objects
    """

    class Meta:
        ordering = ["updated_date"]
        verbose_name = "record"
        verbose_name_plural = "records"

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    reported_timestamp = models.DateTimeField(
        default=timezone.now,
    )
    time_to_live = models.DurationField(default=timedelta(days=90))
    is_recent = models.BooleanField(default=True)
    is_trusted = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    def get_default_comment():
        return "This is a default comment."

    comment = models.TextField(max_length=256, default=get_default_comment)
    type = models.CharField(
        choices=RECORD_TYPES,
        default="",
        max_length=144,
        blank=True,
    )

    def get_default_raw_data():
        return {"key_1": "Value 1", "next_value": "Next Value"}

    raw_data = models.JSONField(
        encoder=DjangoJSONEncoder,
        default=get_default_raw_data,
    )
    # add file upload (PDF, JPG)

    def __str__(self):
        return f"{self.type} ID: {self.pk}"
