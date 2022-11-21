from rest_framework import serializers

from .models import Movie, Record


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_date",
            "updated_date",
        )


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_date",
            "updated_date",
            "reported_timestamp",
        )
