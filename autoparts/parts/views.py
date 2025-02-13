from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.mixins import (
    CreateModelMixin, 
    ListModelMixin, 
    RetrieveModelMixin, 
    UpdateModelMixin, 
    DestroyModelMixin
)
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from autoparts.parts.models import Part, CarParts
from autoparts.parts.tasks import process_parts_from_dataframe
from autoparts.parts.serializers import PartSerializer, CarPartsSerializer, PartsTableSerializer
from autoparts.core.mixins import PermissionsByActionMixin


class PartViewSet(
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    PermissionsByActionMixin,
    GenericViewSet
):
    queryset = Part.objects.all()
    serializer_class = PartSerializer 
    permission_classes_by_action = {
        'create':   [IsAdminUser],
        'update': [IsAdminUser],
        'partial_update': [IsAdminUser],
        'destroy': [IsAdminUser],
        'retrieve': [IsAuthenticated],
        'list': [IsAuthenticated],
    }

    @action(
        detail=False, 
        methods=['POST'], 
        url_path='inport/csv', 
        permission_classes=[AllowAny],
        serializer_class=PartsTableSerializer,
        parser_classes = [MultiPartParser, FormParser]
    )
    def inportdata(self, request):
        file = request.FILES['car_parts_csv']
        path = default_storage.save('tmp/' + file.name, ContentFile(file.read()))
        process_parts_from_dataframe.delay(path)
        return JsonResponse({"message": "Importação sendo processsada"}, status=200)

        


class CarPartsViewSet(
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    PermissionsByActionMixin,
    GenericViewSet
):
    queryset = CarParts.objects.all()
    serializer_class = CarPartsSerializer 
    permission_classes_by_action = {
        'create':   [IsAdminUser],
        'destroy': [IsAdminUser],
        'retrieve': [IsAuthenticated],
        'list': [IsAuthenticated],
    }
