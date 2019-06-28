from .models import Food
from django import forms


class FoodForm(forms.Form):
    name = forms.CharField(max_length=255)
    carbohydrates_amount = forms.IntegerField()
    fats_amount = forms.IntegerField()
    proteins_amount = forms.IntegerField()


class SearchFoodForm(forms.Form):
    food_name = forms.CharField(max_length=100)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)


class RegisterForm(forms.Form):
    fullname = forms.CharField(max_length=255)
    email = forms.EmailField()
    password = forms.CharField(max_length=255)
