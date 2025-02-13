from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin, 
    ListModelMixin, 
    RetrieveModelMixin, 
    UpdateModelMixin, 
    DestroyModelMixin
)

from autoparts.cars.models import Car
from autoparts.cars.serializers import CarSerializer
from autoparts.core.mixins import PermissionsByActionMixin

class CarViewSet(
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    PermissionsByActionMixin,
    GenericViewSet
):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes_by_action = {
        'create':   [IsAdminUser],
        'update': [IsAdminUser],
        'partial_update': [IsAdminUser],
        'destroy': [IsAdminUser],
        'retrieve': [IsAuthenticated],
        'list': [IsAuthenticated],
    }
