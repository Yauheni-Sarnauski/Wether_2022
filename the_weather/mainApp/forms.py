from django.forms import ModelForm, TextInput
from .models import City


class CityForm(ModelForm):  # добовляем город через данную  форму
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'}),
        }