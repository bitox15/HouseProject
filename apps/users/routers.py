from rest_framework.routers import DefaultRouter
from apps.users.api.views import UserViewSet

router = DefaultRouter()

router.register(r'', UserViewSet, basename = 'User')

urlpatterns = router.urls