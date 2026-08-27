from django.contrib import admin
from .models import (Category,Story,StorySection,StorySectionImage,)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]

    search_fields = [
        "name",
    ]

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = [
        "woman_name",
        "title",
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

class StorySectionImageInline(admin.TabularInline):

    model = StorySectionImage

    extra = 1

    fields = [
        "image",
        "caption",
        "alt_text",
        "order",
    ]

    ordering = [
        "order",
    ]

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