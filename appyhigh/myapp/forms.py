from django import forms
from .models import Food
from django import forms


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = "__all__"
