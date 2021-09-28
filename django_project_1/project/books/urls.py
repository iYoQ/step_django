from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('books/', BooksView.as_view(), name='books'),
    path('publishings/', show_publishings, name='publishings'),
    path('forms/', show_forms, name='forms'),
    path('authors/', AuthorView.as_view(), name='authors'),
    path('books/<int:id_book>/', open_book, name='book'),
    path('logout/', logout_view, name='logout')
]
