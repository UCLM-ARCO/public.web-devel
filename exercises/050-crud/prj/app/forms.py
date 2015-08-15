# -*- coding: utf-8; mode: python -*-

from datetime import datetime
from django import forms
from models import Brand

text_ui = forms.TextInput(attrs={'class': 'form-control'})

year_min = 1950
year_max = datetime.now().year
year_ui = forms.NumberInput(
    attrs={'class': 'form-control', 'min': year_min, 'max': year_max})

brand_ui = forms.Select(attrs={'class': 'form-control'})


class VehicleForm(forms.Form):
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), widget=brand_ui)
    model = forms.CharField(max_length=30, widget=text_ui)
    plate = forms.CharField(max_length=12, widget=text_ui)

    year = forms.IntegerField(
        widget=year_ui, min_value=year_min, max_value=year_max)
