from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Book, Booking
from accounts.models import Accounts


def index(request):
    context = {
        'readers': Accounts.objects.all()
    }
    return render(request, template_name='index.html', context=context)


def render_choice(request, reader_id):
    return render(request, template_name='choice.html')


def render_books_active(request, reader_id):
    context = {
        'books': Book.objects.filter(is_active=True)
    }
    return render(request, template_name='books_active.html', context=context)


def take_book(request, book_id, reader_id):
    book = Book.objects.get(id=book_id)
    reader = Accounts.objects.get(id=reader_id)
    booking = Booking.objects.create(book=book, reader=reader)
    book.is_active = False
    book.save()

    return redirect('index')


def render_return_book(request, reader_id):
    reader = Accounts.objects.get(id=reader_id)
    books = []
    for booking in reader.bookings.all():
        if not booking.return_at:
            books.append(booking.book)
    
    context = {
        'books': books
    }

    return render(request, template_name='return_book.html', context=context)


def return_book(request, reader_id, book_id):
    book = Book.objects.get(id=book_id)
    reader = Accounts.objects.get(id=reader_id)
    booking = Booking.objects.get(book=book, reader=reader)
    booking.return_at = timezone.now()
    book.is_active = True
    book.save()
    booking.save()

    return redirect('index')
