from django.contrib import admin
from django.urls import path
from .views import author_form, index, show_books, show_publishings

urlpatterns = [
    path('', index),
    path('books', show_books, name='books'),
    path('publishings', show_publishings, name='publishings'),
    path('author_form/', author_form, name='author_form'),
]
