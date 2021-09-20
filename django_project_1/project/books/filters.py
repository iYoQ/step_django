from django.db.models.enums import Choices
<<<<<<< HEAD
from django.forms import widgets
import django_filters
from django import forms
from django_filters.filters import RangeFilter
from .models import Authors, Books
=======
import django_filters
from django import forms
from .models import Books
>>>>>>> f58b386e285854b118b683cca142183403c98e56


class BooksFilter(django_filters.FilterSet):
    book_names = Books.objects.all()

    name = django_filters.MultipleChoiceFilter(widget=forms.CheckboxSelectMultiple(), choices=[(book.name, book.name) for book in book_names])
<<<<<<< HEAD
    write_date = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'placeholder': 'YYYY-MM-DD'}))
=======
    write_date = django_filters.DateRangeFilter()
>>>>>>> f58b386e285854b118b683cca142183403c98e56


    class Meta:
        model = Books()
<<<<<<< HEAD
        fields = ['name', 'write_date']


class AuthorsFilter(django_filters.FilterSet):
    authors_names = Authors.objects.all()

    name = django_filters.MultipleChoiceFilter(widget=forms.CheckboxSelectMultiple(), choices=[(author, author) for author in authors_names])
    city = django_filters.MultipleChoiceFilter(widget=forms.CheckboxSelectMultiple(), choices=[(author.city, author.city) for author in authors_names])
    birthday = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'placeholder': 'YYYY-MM-DD'}))

    class Meta:
        model = Books()
        fields = ['name', 'city', 'birthday']
=======
        fields = ['name', 'write_date']
>>>>>>> f58b386e285854b118b683cca142183403c98e56
