from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin
from .models import Story, Category


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Story)
class StoryAdmin(ModelAdmin):
    list_display = (
        "cover_preview",
        "woman_name",
        "title",
        "category",
        "country",
        "city",
        "featured",
        "hero_story",
        "published_date",
    )
    list_filter = (
        "category",
        "country",
        "city",
        "featured",
        "hero_story",
        "published_date",
    )
    search_fields = (
        "woman_name",
        "title",
        "summary",
        "country",
        "city",
        "location",
    )
    prepopulated_fields = {
        "slug": ("woman_name", "title"),
    }
    readonly_fields = (
        "created_at",
        "updated_at",
        "cover_preview",
    )
    list_editable = ("featured", "hero_story")
    ordering = ("-published_date", "-created_at")

    fieldsets = (
        (
            "Story Information",
            {
                "fields": (
                    "title",
                    "woman_name",
                    "quote",
                    "summary",
                    "story_content",
                    "category",
                )
            },
        ),
        (
            "Location",
            {
                "fields": (
                    "country",
                    "city",
                    "location",
                )
            },
        ),
        (
            "Publication Settings",
            {
                "fields": (
                    "read_time",
                    "featured",
                    "hero_story",
                    "published_date",
                )
            },
        ),
        (
            "Cover Image",
            {
                "fields": (
                    "cover_image",
                    "cover_preview",
                )
            },
        ),
        (
            "URL Slug",
            {
                "fields": ("slug",),
            },
        ),
        (
            "Timestamps",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                ),
                "classes": ["collapse"],
            },
        ),
    )

    def cover_preview(self, obj):
        if obj.cover_image:
            return format_html(
                '<img src="{}" width="100" height="60" '
                'style="object-fit: cover; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.3);" />',
                obj.cover_image.url,
            )
        return "No image"

    cover_preview.short_description = "Cover"