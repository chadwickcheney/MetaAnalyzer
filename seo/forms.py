from django.forms import ModelForm, TextInput
from .models import Url

class UrlForm(ModelForm):
    class Meta:
        model = Url
        fields = ['address']
        widgets = {'name' : TextInput (attrs={'class' : 'input', 'placeholder' : 'Url'})}
