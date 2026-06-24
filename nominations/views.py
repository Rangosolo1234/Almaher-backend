from rest_framework import viewsets
from .models import Nomination
from .serializers import NominationSerializer

class NominationViewSet(viewsets.ModelViewSet):
    queryset = Nomination.objects.all().order_by("-created_at")
    serializer_class = NominationSerializer