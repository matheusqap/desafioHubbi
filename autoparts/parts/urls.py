from rest_framework import routers

from autoparts.parts.views import PartViewSet, CarPartsViewSet

router = routers.DefaultRouter()
router.register(r'carparts', CarPartsViewSet, basename='CarPartsViewSet')
router.register(r'', PartViewSet, basename='PartViewSet')

app_name = 'parts'
urlpatterns = []
urlpatterns += router.urls