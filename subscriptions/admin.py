from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Subscriber


@admin.register(Subscriber)
class SubscriberAdmin(ModelAdmin):
    list_display = ("email", "active", "subscribed_at")
    list_filter = ("active", "subscribed_at")
    search_fields = ("email",)
    list_editable = ("active",)
    readonly_fields = ("subscribed_at",)