from django import forms
from .models import mymodel


class mymodelform(forms.ModelForm):
    class Meta:
        model = mymodel
        fields = ['name' , 'email']