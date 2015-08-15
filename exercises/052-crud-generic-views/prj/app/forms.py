# -*- coding: utf-8; mode: python -*-

from datetime import datetime
from django import forms

from .models import Vehicle

text_ui = forms.TextInput(attrs={'class': 'form-control', 'autofocus': True})

year_min = 1950
year_max = datetime.now().year
year_ui = forms.NumberInput(
    attrs={'class': 'form-control', 'min': year_min, 'max': year_max})

brand_ui = forms.Select(attrs={'class': 'form-control'})


class VehicleForm(forms.ModelForm):

    class Meta:
        model = Vehicle
        fields = '__all__'
        widgets = dict(brand=brand_ui, model=text_ui, plate=text_ui)

    year = forms.IntegerField(
        widget=year_ui, min_value=year_min, max_value=year_max)
