from rest_framework.routers import DefaultRouter
from apps.users.api.views import UserAPIModelViewSet

router = DefaultRouter()
router.register(r"",UserAPIModelViewSet, basename="users")
urlpatterns = router.urls