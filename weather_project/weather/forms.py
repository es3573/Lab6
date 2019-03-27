from django.forms import ModelForm, TextInput
from .models import City

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name', 'option']
        widgets = {
                'name': TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'}),
                'option': TextInput(attrs={'class' : 'input', 'placeholder' : '[1,2,3]'})
                }
        

