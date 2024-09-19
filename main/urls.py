from django.urls import path

from main.views import CarBrandListView, BrandDetailView, CarDetailView, CarsView, create_car_view, send_email_view


urlpatterns = [
    path('brands/', CarBrandListView.as_view(), name='brands'),
    path('cars/', CarsView.as_view(), name='cars'),
    path('cars/create/', create_car_view, name='car_create'),
    path('brands/<int:pk>/', BrandDetailView.as_view(), name='brand_detail'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('send-mail/', send_email_view, name='email'),
]