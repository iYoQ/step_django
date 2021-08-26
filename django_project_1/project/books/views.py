from django.shortcuts import render
from .models import Authors, Books, Publishings
from .forms import FormAuthors

def index(request):
    context = {'books': 'show books', 'publishing': 'show publishing', 'author_form': 'author form'}
    return render(request, 'books/index.html', context=context)

def show_books(request):

    books = Books.objects.all()

    context = {'books': books}

    return render(request, 'books/books.html', context=context)

def show_publishings(request):

    publishings = Publishings.objects.all()
    books = Books.objects.all()

    context = {'publishings': publishings, 'books': books}

    return render(request, 'books/publishings.html', context=context)

def author_form(request):
    
    if request.method == 'POST':
        form = FormAuthors(request.POST)
        if form.is_valid() and form.is_bound:
            name = form.cleaned_data['name']
            surename = form.cleaned_data['surename']
            fathername = form.cleaned_data['fathername']
            city = form.cleaned_data['city']
            birthday = form.cleaned_data['birthday']

            author = Authors(name=name, surename=surename, fathername=fathername, city=city, birthday=birthday)
            author.save()
    else:
        form = FormAuthors

    context = {'form': form, }

    return render(request, 'books/form.html', context=context)