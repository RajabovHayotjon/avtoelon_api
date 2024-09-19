from rest_framework import serializers

from main.models import Car, CarBrand


class CarBrandSerializer(serializers.ModelSerializer):
    car_count = serializers.SerializerMethodField()

    def get_car_count(self, obj):
        return obj.cars.all().count()

    class Meta:
        model = CarBrand
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
    

class CarBrandSingleSerializer(serializers.ModelSerializer):
    car_count = serializers.SerializerMethodField()
    cars = serializers.SerializerMethodField()

    def get_car_count(self, obj):
        return obj.cars.all().count()

    def get_cars(self, obj):
        serializer = CarSerializer(obj.cars.all(), many=True)
        return serializer.data

    class Meta:
        model = CarBrand
        fields = '__all__'



