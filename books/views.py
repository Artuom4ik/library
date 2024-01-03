from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Book, Booking
from accounts.models import Accounts


def index(request):
    context = {
        'readers': Accounts.objects.all()
    }
    return render(request, template_name='index.html', context=context)


def render_choice(request):
    print(request.user)
    return render(request, template_name='choice.html')


def render_books_active(request):
    context = {
        'books': Book.objects.filter(is_active=True)
    }
    return render(request, template_name='books_active.html', context=context)


def take_book(request, book_id):
    book = Book.objects.get(id=book_id)
    reader = Accounts.objects.get(username=request.user)
    Booking.objects.create(book=book, reader=reader)
    book.is_active = False
    book.save()

    return redirect('books:choice')


def render_return_book(request):
    username = request.user

    reader = Accounts.objects.get(username=username)
    books = []

    for booking in reader.bookings.all():
        if not booking.return_at:
            books.append(booking.book)
    
    context = {
        'books': books
    }

    return render(request, template_name='return_book.html', context=context)


def return_book(request, book_id):
    book = Book.objects.get(id=book_id)
    reader = Accounts.objects.get(username=request.user)
    booking = Booking.objects.get(book=book, reader=reader, return_at=None)
    booking.return_at = timezone.now()
    book.is_active = True
    book.save()
    booking.save()

    return redirect('books:choice')
