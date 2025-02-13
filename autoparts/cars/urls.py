from rest_framework import routers

from autoparts.cars.views import CarViewSet

router = routers.DefaultRouter()
router.register(r'', CarViewSet, basename='CarViewSet')

app_name = 'cars'
urlpatterns = []
urlpatterns += router.urls