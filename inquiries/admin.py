from django.contrib import admin
from .models import Inquiry

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "category",
        "country",
        "city",
        "created_at",
    )

    list_filter = (
        "category",
        "country",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "organization_name",
        "country",
        "city",
        "message",
    )

    readonly_fields = (
        "created_at",
    )

    ordering = ("-created_at",)