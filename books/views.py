from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Book, Booking
from accounts.models import Account


def index(request):
    context = {
        'readers': Account.objects.all()
    }

    return render(request, template_name='index.html', context=context)


def render_choice(request):
    return render(request, template_name='choice.html')


def render_books_active(request):
    context = {
        'books': Book.objects.filter(is_active=True)
    }
    
    return render(request, template_name='books_active.html', context=context)


def take_book(request, book_id):
    book = Book.objects.get(id=book_id)
    reader = Account.objects.get(user=request.user)
    Booking.objects.create(book=book, reader=reader)
    book.is_active = False
    book.save()

    return redirect('books:choice')


def render_return_book(request):
    reader = Account.objects.get(user=request.user)
    
    context = {
        'books': reader.bookings.filter(return_at=None)
    }

    return render(request, template_name='return_book.html', context=context)


def return_book(request, book_id):
    book = Book.objects.get(id=book_id)
    reader = Account.objects.get(user=request.user)
    booking = Booking.objects.get(book=book, reader=reader, return_at=None)
    booking.return_at = timezone.now()
    book.is_active = True
    book.save()
    booking.save()

    return redirect('books:choice')
