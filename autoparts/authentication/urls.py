from rest_framework import routers
from rest_framework.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from autoparts.authentication.views import UserViewSet, AdminAuthViewSet

app_name = "authentication"
router = routers.DefaultRouter()
router.register('user', UserViewSet, basename='UserViewSet')
router.register('admin', AdminAuthViewSet, basename='AdminAuthViewSet')


urlpatterns = [
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]

urlpatterns += router.urls


