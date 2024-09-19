from django_filters import rest_framework as filters
from main.models import Car


class CarFilter(filters.FilterSet):
    price_gte = filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_lte = filters.NumberFilter(field_name='price', lookup_expr='lte')
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Car
        fields = ['name', 'brand', 'price_gte', 'price_lte', 'category']