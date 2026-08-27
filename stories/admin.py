from django.contrib import admin
from .models import (Category,Story,StorySection,StorySectionImage,)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = [
        "woman_name",
        "title",
        "author_name",
        "category",
        "country",
        "city",
        "featured",
        "hero_story",
        "published_date",
    ]

    list_filter = [
        "category",
        "featured",
        "hero_story",
        "country",
        "published_date",
    ]

    search_fields = [
        "woman_name",
        "title",
        "author_name",
        "role_or_subtitle",
        "summary",
        "story_content",
    ]

    prepopulated_fields = {
        "slug": ("woman_name", "title"),
    }

    readonly_fields = [
        "created_at",
        "updated_at",
    ]

    fieldsets = (
        ("Story Details", {
            "fields": (
                "title",
                "woman_name",
                "role_or_subtitle",
                "slug",
                "category",
                "quote",
                "summary",
                "story_content",
                "cover_image",
            )
        }),
        ("Author / Documenter", {
            "fields": (
                "author_name",
                "author_image",
            ),
            "description": "Upload the photographer/writer avatar and their full name here.",
        }),
        ("Location & Meta", {
            "fields": (
                "country",
                "city",
                "location",
                "read_time",
                "published_date",
                "featured",
                "hero_story",
            )
        }),
        ("Timestamps", {
            "fields": (
                "created_at",
                "updated_at",
            ),
            "classes": ("collapse",),
        }),
    )

class StorySectionImageInline(admin.TabularInline):
    model = StorySectionImage
    extra = 1
    fields = [
        "image",
        "caption",
        "alt_text",
        "order",
    ]
    ordering = ["order"]


@admin.register(StorySection)
class StorySectionAdmin(admin.ModelAdmin):
    list_display = [
        "story",
        "heading",
        "layout",
        "order",
    ]

    list_filter = [
        "layout",
    ]

    search_fields = [
        "story__woman_name",
        "story__title",
        "heading",
        "content",
    ]

    ordering = [
        "story",
        "order",
    ]

    inlines = [
        StorySectionImageInline,
    ]