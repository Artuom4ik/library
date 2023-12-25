from django.contrib import admin

from .models import Author, Reader, Book
# Register your models here.

class BookModelInline(admin.StackedInline):
    model = Book
    fields = ('code', 'title',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookModelInline]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    pass
