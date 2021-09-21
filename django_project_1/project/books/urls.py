from django.contrib import admin
from django.urls import path
from .views import show_forms, index, show_books, show_publishings, show_authors, open_book

urlpatterns = [
    path('', index),
    path('books', show_books, name='books'),
    path('publishings/', show_publishings, name='publishings'),
    path('forms/', show_forms, name='forms'),
    path('authors/', show_authors, name='authors'),
    path('books/<int:id_book>/', open_book, name='book'),
]
