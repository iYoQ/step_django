from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Authors, Books, Publishings
from .forms import AddAuthorForm, AddBookForm
<<<<<<< HEAD
from .filters import BooksFilter, AuthorsFilter
=======
from .filters import BooksFilter
>>>>>>> f58b386e285854b118b683cca142183403c98e56

def index(request):
    context = {'books': 'show books', 'publishing': 'show publishing', 'forms': 'show forms', 'authors': 'show authors',}
    return render(request, 'books/index.html', context=context)

def show_books(request):
    books = Books.objects.all()
    books_filter = BooksFilter(request.GET, queryset=books)

    context = {'books': books, 'books_filter': books_filter}

    return render(request, 'books/books.html', context=context)

def show_publishings(request):

    publishings = Publishings.objects.all()
    books = Books.objects.all()

    context = {'publishings': publishings, 'books': books}

    return render(request, 'books/publishings.html', context=context)

def show_forms(request):
    author_form = AddAuthorForm()
    book_form = AddBookForm()

    if request.method == 'POST' and 'send_author' in request.POST:
        author_form = AddAuthorForm(request.POST)

        if author_form.is_valid() and author_form.is_bound:
            name = author_form.cleaned_data['name']
            surename = author_form.cleaned_data['surename']
            fathername = author_form.cleaned_data['fathername']
            city = author_form.cleaned_data['city']
            birthday = author_form.cleaned_data['birthday']

            Authors(name=name, surename=surename, fathername=fathername, city=city, birthday=birthday).save()
            author_form = AddAuthorForm()

            return HttpResponseRedirect('forms')

    elif request.method == 'POST' and 'send_book' in request.POST:
        book_form = AddBookForm(request.POST, request.FILES)

        if book_form.is_valid() and book_form.is_bound:
            name = book_form.cleaned_data['name']
            write_date = book_form.cleaned_data['write_date']
            description = book_form.cleaned_data['description']
            pages = book_form.cleaned_data['pages']
            image = book_form.cleaned_data['image']
            author_relative = Authors.objects.get(id=book_form.cleaned_data['author_relative'])
            publishing_relative = Publishings.objects.get(id=book_form.cleaned_data['publishing_relative'])

            Books(name=name, write_date=write_date, description=description, pages=pages, image=image, author_relative=author_relative, publishing_relative=publishing_relative).save()
            book_form = AddBookForm()

            return HttpResponseRedirect('forms')

    context = {'author_form': author_form, 'book_form': book_form}

    return render(request, 'books/forms.html', context=context)

def show_authors(request):
    authors_filter = AuthorsFilter(request.GET, queryset=Authors.objects.all())
    books = Books.objects.all()

    context = {'authors_filter': authors_filter, 'books': books}

    return render(request, 'books/authors.html', context=context)