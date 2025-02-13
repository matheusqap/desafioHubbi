from rest_framework import serializers

from autoparts.parts.models import Part, CarParts

class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = [
            'id',
            'part_number',
            'name',
            'details',
            'price',
            'quantity'
        ]

class CarPartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarParts
        fields = [
            'id',
            'part',
            'car'
        ]

class PartsTableSerializer(serializers.Serializer):
    car_parts_csv = serializers.FileField(required=True)
    class Meta:
        model = CarParts
        fields = [
            'car_parts_csv'
        ]