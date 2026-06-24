from rest_framework.routers import DefaultRouter
from .views import NominationViewSet

router = DefaultRouter()

router.register(r"nominations", NominationViewSet, basename="nomination"
)
urlpatterns = router.urls