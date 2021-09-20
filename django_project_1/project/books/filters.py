from django.forms import widgets
from django import forms
from .models import Authors, Books
import django_filters


class BooksFilter(django_filters.FilterSet):
    book_names = Books.objects.all()

    name = django_filters.MultipleChoiceFilter(widget=forms.CheckboxSelectMultiple(), choices=[(book.name, book.name) for book in book_names])
    write_date = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'placeholder': 'YYYY-MM-DD'}))


    class Meta:
        model = Books()
        fields = ['name', 'write_date']


class AuthorsFilter(django_filters.FilterSet):
    authors_names = Authors.objects.all()

    surename = django_filters.MultipleChoiceFilter(widget=forms.CheckboxSelectMultiple(), choices=[(author.surename, author.surename) for author in authors_names])
    city = django_filters.MultipleChoiceFilter(widget=forms.CheckboxSelectMultiple(), choices=[(author.city, author.city) for author in authors_names])
    birthday = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'placeholder': 'YYYY-MM-DD'}))

    class Meta:
        model = Books()
        fields = ['surename', 'city', 'birthday']
