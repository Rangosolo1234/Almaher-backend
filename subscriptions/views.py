from rest_framework import viewsets
from .models import Subscriber
from .serializers import SubscriberSerializer

class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all().order_by("-subscribed_at")
    serializer_class = SubscriberSerializer