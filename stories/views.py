from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser

from .models import Story, Category
from .serializers import (
    StoryListSerializer,
    StoryDetailSerializer,
    CategorySerializer,
)

class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all().order_by("-published_date")
    lookup_field = "slug"

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return StoryDetailSerializer

        return StoryListSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]