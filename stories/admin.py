from django.contrib import admin
from django.utils.html import format_html
from .models import Story, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ( "name",)
    search_fields = ("name",)
    ordering = ("name",)

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = (
        "woman_name",
        "title",
        "category",
        "country",
        "city",
        "featured",
        "hero_story",
        "published_date",
        "cover_preview",
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
        "slug": (
            "woman_name",
            "title",
        ),
    }

    readonly_fields = (
        "created_at",
        "updated_at",
        "cover_preview",
    )

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
            "Publication",
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
            "URL",
            {
                "fields": (
                    "slug",
                )
            },
        ),
        (
            "Timestamps",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    ordering = (
        "-published_date",
        "-created_at",
    )

    def cover_preview(self, obj):
        if obj.cover_image:
            return format_html(
                '<img src="{}" width="120" height="80" '
                'style="object-fit: cover; border-radius: 6px;" />',
                obj.cover_image.url,
            )

        return "No image"

    cover_preview.short_description = "Cover"