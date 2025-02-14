from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny


schema_view = get_schema_view(
    openapi.Info(
        title='Autoparts Service API',
        default_version='v1',
        description='Autoparts Service API',
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('dashboard/admin', admin.site.urls),
    path('auth/', include('autoparts.authentication.urls', namespace='authentication')),
    path('cars/', include('autoparts.cars.urls', namespace='cars')),
    path('parts/', include('autoparts.parts.urls', namespace='parts')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]