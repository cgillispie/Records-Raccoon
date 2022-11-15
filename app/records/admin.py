from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import Movie, CustomUser, Record


@admin.register(CustomUser)
class UserAdmin(DefaultUserAdmin):
    pass


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = (
        "title", "genre", "year", "created_date", "updated_date",
    )
    list_display = (
        "title", "genre", "year", "created_date", "updated_date",
    )
    readonly_fields = (
        "created_date", "updated_date",
    )


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    fields = (
        "type", "is_active", "reported_timestamp", "comment", "updated_date", "raw_data", 

    )
    list_display = (
        "type", "is_active", "reported_timestamp", "comment", "updated_date", "raw_data",
    )
    readonly_fields = (
        "created_date", "updated_date", "reported_timestamp", 
    )