from django.contrib import admin
from .models import Nomination

@admin.register(Nomination)
class NominationAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "country",
        "city",
        "submitted_by_name",
        "submitted_by_email",
        "reviewed",
        "created_at",
    )

    list_filter = (
        "reviewed",
        "country",
        "city",
        "created_at",
    )

    search_fields = (
        "full_name",
        "country",
        "city",
        "submitted_by_name",
        "submitted_by_email",
        "what_she_is_doing",
    )

    readonly_fields = (
        "created_at",
    )

    ordering = ("-created_at",)