from django import forms
from .models import ClienteModels

class ClienteForm(forms.ModelForm):
    class Meta:
        model = ClienteModels
        fields = '__all__'