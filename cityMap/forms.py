from django import forms
from .models import CityOwned


class CityOwnedForm(forms.ModelForm):
    class Meta:
        model = CityOwned
        fields = ['city_name', ]
