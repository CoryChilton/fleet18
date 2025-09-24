from rest_framework import routers
from events.views import EventViewSet

router = routers.DefaultRouter()
router.register('api/events', EventViewSet, 'events')

urlpatterns = router.urls