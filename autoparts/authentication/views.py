from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response

from autoparts.authentication.models import User
from autoparts.authentication.serializers import UserSerializer, LoginSerializer
from autoparts.authentication.utils import get_tokens_for_user
from autoparts.core.mixins import PermissionsByActionMixin


class UserViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    PermissionsByActionMixin,
    GenericViewSet
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes_by_action = {
        'create': [AllowAny],
        'retrieve': [IsAuthenticated],
    }

class AdminAuthViewSet(GenericViewSet):

    queryset = User.objects.all()
    serializer_class = LoginSerializer

    @action(detail=False, methods=['POST'], url_path='signin', permission_classes=[AllowAny])
    def signin(self, request):
        try: 
            user = get_object_or_404(User, username=request.data.get('username'))

            if not user.is_superuser or not check_password(request.data.get('password'), user.password):
                return Response('Authentication User Not Found', status=status.HTTP_404_NOT_FOUND)

            tokens = get_tokens_for_user(user)

            return Response(tokens, status=status.HTTP_200_OK)

        except Exception as error:
            raise ValidationError(error)