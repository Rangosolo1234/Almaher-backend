from rest_framework import viewsets
from .models import Story, Category
from .serializers import (StorySerializer, CategorySerializer)

class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all().order_by("-published_date")
    serializer_class = StorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer