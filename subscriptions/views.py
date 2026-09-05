from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.throttling import ScopedRateThrottle
from .models import Subscriber
from .serializers import SubscriberSerializer

class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all().order_by("-subscribed_at")
    serializer_class = SubscriberSerializer

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

    throttle_scope = "subscription"