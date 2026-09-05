from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.throttling import ScopedRateThrottle
from .models import Inquiry
from .serializers import InquirySerializer

class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all().order_by("-created_at")
    serializer_class = InquirySerializer

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

    throttle_scope = "contact"