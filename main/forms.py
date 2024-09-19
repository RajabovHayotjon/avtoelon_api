from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'produced_year', 'color', 'price', 'case', 'location', 'brand', 'fuel', 'category']