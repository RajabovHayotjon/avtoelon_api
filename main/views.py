from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView

from main.filters import CarFilter
from main.models import Car, CarBrand
from main.serializers import CarBrandSerializer, CarBrandSingleSerializer, CarSerializer
from django.shortcuts import render, redirect
from .forms import CarForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


class CarBrandListView(ListAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer


class BrandDetailView(RetrieveAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSingleSerializer


class CarsView(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['brand', 'price', 'name', 'price__gte', 'price__lte']
    filterset_class = CarFilter


class CarDetailView(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


@api_view(['POST'])
def create_car_view(request):
    if request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            car = serializer.save(user=request.user)  # Set the current user
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def send_email_view(request):
    send_mail.delay()
    return Response({'status':'ok'})


