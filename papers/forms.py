from django.forms import ModelForm
from .models import Papers
from django import forms

class SearchPaperForm(forms.Form):
    querycom = forms.CharField(label='Please, enter article title',
    widget=forms.TextInput(attrs={'size': 32, 'class':'form-control'}))
