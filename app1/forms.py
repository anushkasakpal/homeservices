from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from .models import usermodel

class userform(forms.ModelForm):
    class Meta:
        model = usermodel
        fields = '__all__'





