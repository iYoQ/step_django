from django.contrib import admin
from django.urls import path
from .views import show_forms, main, show_books, show_publishings, show_authors, open_book, logout_view

urlpatterns = [
    path('', main, name='main'),
    path('books/', show_books, name='books'),
    path('publishings/', show_publishings, name='publishings'),
    path('forms/', show_forms, name='forms'),
    path('authors/', show_authors, name='authors'),
    path('books/<int:id_book>/', open_book, name='book'),
    path('logout/', logout_view, name='logout')
]
