from django.db.models.enums import Choices
import django_filters
from django import forms
from .models import Books


class BooksFilter(django_filters.FilterSet):
    book_names = Books.objects.all()

    name = django_filters.MultipleChoiceFilter(widget=forms.CheckboxSelectMultiple(), choices=[(book.name, book.name) for book in book_names])
    write_date = django_filters.DateRangeFilter()


    class Meta:
        model = Books()
        fields = ['name', 'write_date']