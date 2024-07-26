# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth import get_user_model

from kitchen.models import Cook, DishType, Dish


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    first_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "First name",
                "class": "form-control"
            }
        ))
    last_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last name",
                "class": "form-control"
            }
        ))
    years_of_experience = forms.IntegerField(
        label='Years of Experience',
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Experience",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    class Meta:
        model = Cook
        fields = ('username', 'email', 'years_of_experience')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name",
                "class": "form-control"
            }
        )
    )


class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                "placeholder": "Name",
                "class": "form-control"
            }),
        }


class CookSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by username",
                "class": "form-control"
            }
        )
    )


class CookUpdateForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    first_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "First name",
                "class": "form-control"
            }
        ))
    last_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last name",
                "class": "form-control"
            }
        ))
    years_of_experience = forms.IntegerField(
        label='Years of Experience',
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Experience",
                "class": "form-control"
            }
        ))

    class Meta:
        model = Cook
        fields = ('username', 'email', 'years_of_experience')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name",
                "class": "form-control"
            }
        )
    )


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Dish
        fields = ['name', 'description', 'price', 'dish_type', 'cooks']
        widgets = {
            'name': forms.TextInput(attrs={
                "placeholder": "Name",
                "class": "form-control"
            }),
            'description': forms.Textarea(attrs={
                "placeholder": "Description",
                "class": "form-control"
            }),
            'price': forms.NumberInput(attrs={
                "placeholder": "Price",
                "class": "form-control"
            }),
            'dish_type': forms.Select(attrs={
                "title": "Dish Type",
                "placeholder": "Dish Type",
                "class": "form-control"
            }),
        }
