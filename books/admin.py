from django.contrib import admin

from .models import Author, Book, Booking
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


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass
