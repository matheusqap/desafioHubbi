from rest_framework import serializers

from autoparts.cars.models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            'id',
            'name',
            'manufacturer',
            'year'
        ]
