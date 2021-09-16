from django.forms.widgets import TextInput
from .models import Authors, Publishings
from django import forms

class AddAuthorForm(forms.Form):
    name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'author name'}))
    surename = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'author surname'}))
    fathername = forms.CharField(max_length=250, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'author fathername'}))
    city = forms.CharField(max_length=250, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'author cityname'}))
    birthday = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'birthday'}))


class AddBookForm(forms.Form):
    authors = Authors.objects.all()
    publishings = Publishings.objects.all()

    name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'book name'}))
    write_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'write date'}))
    description = forms.CharField(max_length=2000, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'book description'}))
    pages = forms.IntegerField(min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'pages'}))
    image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'id': 'image'}))
    author_relative = forms.ChoiceField(choices=[(author.id, author) for author in authors], widget=forms.Select(attrs={'class': 'form-control'}))
    publishing_relative = forms.ChoiceField(choices=[(publishing.id, publishing.name) for publishing in publishings], widget=forms.Select(attrs={'class': 'form-control'}))
