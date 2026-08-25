from django.contrib import admin
from .models import Subscriber

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "active",
        "subscribed_at",
    )

    list_filter = (
        "active",
        "subscribed_at",
    )

    search_fields = (
        "email",
    )

    readonly_fields = (
        "subscribed_at",
    )

    ordering = (
        "-subscribed_at",
    )