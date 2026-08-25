from rest_framework import serializers
from .models import Story, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class StorySerializer(serializers.ModelSerializer):
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
        ]

    def get_cover_image(self, obj):
        if obj.cover_image:
            return obj.cover_image.url
        return None