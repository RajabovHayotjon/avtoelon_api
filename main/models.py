from django.db import models

from accounts.models import User


class CarBrand(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='cars/brands/')

    def __str__(self):
        return self.name


class CarColor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=300)
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    produced_year = models.DateField()
    color = models.ForeignKey(CarColor, models.CASCADE, related_name='cars')
    price = models.PositiveIntegerField()
    case = models.CharField(max_length=200)
    location = models.CharField(max_length=500)
    brand = models.ForeignKey(CarBrand, models.CASCADE, related_name='cars')
    fuel = models.CharField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(Category, models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    car = models.ForeignKey(Car, models.CASCADE, related_name='images')

    def __str__(self):
        return self.car.name
