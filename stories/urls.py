from rest_framework.routers import DefaultRouter
from .views import StoryViewSet, CategoryViewSet

router = DefaultRouter()

router.register("stories",StoryViewSet)
router.register("categories",CategoryViewSet)

urlpatterns = router.urls