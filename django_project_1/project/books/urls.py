from django.contrib import admin
from django.urls import path
from .views import show_forms, index, show_books, show_publishings

urlpatterns = [
    path('', index),
    path('books', show_books, name='books'),
    path('publishings', show_publishings, name='publishings'),
    path('forms', show_forms, name='forms'),
]
