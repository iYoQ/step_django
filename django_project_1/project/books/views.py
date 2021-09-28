from django.shortcuts import render, redirect
from .models import Authors, Books, Publishings
from .forms import AddAuthorForm, AddBookForm
from .filters import BooksFilter, AuthorsFilter
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic import ListView


class BooksView(ListView):
    paginate_by = 2
    model = Books()
    template_name = 'books/books.html'
    queryset = Books.objects.all()


class AuthorView(ListView):
    paginate_by = 2
    model = Authors()
    template_name = 'books/authors.html'
    queryset = Authors.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Books.objects.all()
        return context

@login_required(login_url='home')
def main(request):
    context = {'books': 'show books', 'publishing': 'show publishing', 'forms': 'show forms', 'authors': 'show authors', 'logout': 'logout'}
    return render(request, 'books/main.html', context=context)

# @login_required(login_url='home')
# def show_books(request):
#     books = Books.objects.all()
#     books_filter = BooksFilter(request.GET, queryset=books)

#     context = {'books': books, 'books_filter': books_filter}

#     return render(request, 'books/books.html', context=context)

@login_required(login_url='home')
def show_publishings(request):

    publishings = Publishings.objects.all()
    books = Books.objects.all()

    context = {'publishings': publishings, 'books': books}

    return render(request, 'books/publishings.html', context=context)

@login_required(login_url='home')
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

            return redirect('forms')

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

            return redirect('forms')

    context = {'author_form': author_form, 'book_form': book_form}

    return render(request, 'books/forms.html', context=context)

# @login_required(login_url='home')
# def show_authors(request):
#     authors_filter = AuthorsFilter(request.GET, queryset=Authors.objects.all())
#     books = Books.objects.all()

#     context = {'authors_filter': authors_filter, 'books': books}

#     return render(request, 'books/authors.html', context=context)

@login_required(login_url='home')
def open_book(request, id_book):
    book = Books.objects.get(id=id_book)
    
    context = {'book': book}

    return render(request, 'books/about_book.html', context=context)

def logout_view(request):
    logout(request)
    return redirect('home')