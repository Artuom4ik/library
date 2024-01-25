from django.contrib import admin

from .models import Author, Book, Booking


class BookModelInline(admin.StackedInline):
    model = Book
    fields = ('code', 'title',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookModelInline]


admin.site.register(Book)
admin.site.register(Booking)
