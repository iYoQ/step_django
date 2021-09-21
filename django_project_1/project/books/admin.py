from django.contrib import admin
from .models import Authors, Books, Publishings

class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'surename', 'fathername', 'city', 'birthday')
    list_display_links = ('name', 'surename')
    search_fields = ('name', 'surename')

class BooksAdmin(admin.ModelAdmin):
    list_display = ('name', 'write_date', 'description', 'pages', 'image', 'author_relative', 'publishing_relative')
    list_display_links = ('name',)
    search_fields = ('name',)

class BookInLine(admin.TabularInline):
    model = Books

class PublishingsAdmin(admin.ModelAdmin):
    def list_of_books(self, obj):
        return '; '.join(book.name for book in obj.books_set.all())

    inlines = [BookInLine, ]
    list_display = ('name', 'list_of_books')
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(Authors, AuthorsAdmin)
admin.site.register(Books, BooksAdmin)
admin.site.register(Publishings, PublishingsAdmin)
