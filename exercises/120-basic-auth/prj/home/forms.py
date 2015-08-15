# -*- coding: utf-8; mode: python; -*-

from django.contrib.auth import forms as auth_forms, models as auth_models
from django import forms


text_ui = forms.TextInput(attrs={'class': 'form-control', 'autofocus': True})
email_ui = forms.EmailInput(attrs={'class': 'form-control'})


class UserCreationForm(auth_forms.UserCreationForm):
    password1 = forms.CharField(
        label = "Password",
        widget = forms.PasswordInput(attrs={'class': 'form-control'}))

    password2 = forms.CharField(
        label = "Password confirmation",
        widget = forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text = "Enter the same password as above, for verification.")

    class Meta:
        model = auth_models.User
        fields = ("username", 'first_name', 'last_name', 'email')
        widgets = dict(
            username = text_ui,
            first_name = text_ui,
            last_name = text_ui,
            email = email_ui,
            password1 = text_ui,
        )
