from rest_framework import viewsets
from .models import Story, Category
from .serializers import (StoryListSerializer, StoryDetailSerializer, CategorySerializer,)

class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all().order_by("-published_date")
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action == "retrieve":
            return StoryDetailSerializer

        return StoryListSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer