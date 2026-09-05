from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.throttling import ScopedRateThrottle
from .models import Nomination
from .serializers import NominationSerializer

class NominationViewSet(viewsets.ModelViewSet):
    queryset = Nomination.objects.all().order_by("-created_at")
    serializer_class = NominationSerializer

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]

    def get_throttles(self):
        if self.action == "create":
            return [ScopedRateThrottle()]
        return super().get_throttles()
    
    throttle_scope = "nomination"