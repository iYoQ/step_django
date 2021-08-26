from django.forms.widgets import TextInput
from .models import Authors
from django import forms

class FormAuthors(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'author name'}))
    surename = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'author surname'}))
    fathername = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'author fathername'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'author cityname'}))
    birthday = forms.DateField(widget=forms.DateInput(attrs={'placeholder': '24-08-2021'})) 