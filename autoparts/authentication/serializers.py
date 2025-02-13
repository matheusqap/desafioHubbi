from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from autoparts.authentication.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        create_only_fields = [
            'email',
            'username',
            'password',
        ]
        fields = [
            'id', 
            'email', 
            'username', 
            'password',
            'name',
        ]

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]