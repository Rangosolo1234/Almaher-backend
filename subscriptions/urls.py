from rest_framework.routers import DefaultRouter
from .views import SubscriberViewSet

router = DefaultRouter()

router.register(r"subscribers", SubscriberViewSet, basename="subscriber")
urlpatterns = router.urls