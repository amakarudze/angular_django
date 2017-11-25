from .api import VideoViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'videos', VideoViewSet)

urlpatterns = router.urls