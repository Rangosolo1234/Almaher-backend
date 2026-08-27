from rest_framework import serializers

from .models import (
    Story,
    Category,
    StorySection,
    StorySectionImage,
)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class StorySectionImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = StorySectionImage
        fields = [
            "id",
            "image",
            "caption",
            "alt_text",
            "order",
        ]

    def get_image(self, obj):
        if obj.image:
            return obj.image.url

        return None


class StorySectionSerializer(serializers.ModelSerializer):
    images = StorySectionImageSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = StorySection
        fields = [
            "id",
            "heading",
            "content",
            "layout",
            "order",
            "images",
        ]


class StoryListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source="category.name",
        read_only=True,
        default="",
    )
    cover_image = serializers.SerializerMethodField()

    class Meta:
        model = Story
        fields = [
            "id",
            "title",
            "woman_name",
            "quote",
            "summary",
            "category",
            "category_name",
            "country",
            "city",
            "location",
            "read_time",
            "featured",
            "hero_story",
            "cover_image",
            "slug",
            "published_date",
            "created_at",
            "updated_at",
        ]

    def get_cover_image(self, obj):
        if obj.cover_image:
            return obj.cover_image.url

        return None


class StoryDetailSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True,default="",)
    cover_image = serializers.SerializerMethodField()
    sections = StorySectionSerializer(many=True,read_only=True)
    author_image = serializers.SerializerMethodField()

    class Meta:
        model = Story
        fields = [
            "id",
            "title",
            "woman_name",
            "quote",
            "summary",
            "story_content",
            "category",
            "category_name",
            "country",
            "city",
            "location",
            "read_time",
            "featured",
            "hero_story",
            "cover_image",
            "slug",
            "published_date",
            "created_at",
            "updated_at",
            "sections",
            "author_name",
            "author_image",
            "role_or_subtitle",
        ]

    def get_author_image(self, obj):
        if obj.author_image:
            return obj.author_image.url
        return None

    def get_cover_image(self, obj):
        if obj.cover_image:
            return obj.cover_image.url

        return None