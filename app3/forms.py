from django import forms
from .models import adminmodel

class servicemenForm(forms.ModelForm):
    class Meta:
        model = adminmodel
        fields = '__all__'
        #labels = {}
