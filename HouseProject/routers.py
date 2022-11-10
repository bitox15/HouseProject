from rest_framework.routers import DefaultRouter
from apps.users.api.views import UserViewSet
from apps.housing.api.views import HousingViewSet

router = DefaultRouter()

router.register(r'user', UserViewSet, basename = 'User')
router.register(r'housing', HousingViewSet, basename = 'housing')
urlpatterns = router.urls