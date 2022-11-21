# Generated by Django 4.1.2 on 2022-11-10 19:50

import django.core.serializers.json
from django.db import migrations, models

import records.models


class Migration(migrations.Migration):

    dependencies = [
        ("records", "0004_alter_record_raw_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="record",
            name="raw_data",
            field=models.JSONField(
                default=records.models.Record.get_default_raw_data,
                encoder=django.core.serializers.json.DjangoJSONEncoder,
            ),
        ),
    ]
