from django.shortcuts import render

from .models import Book, Author
from accounts.models import Accounts


def index(request):
    context = {
        'readers': Accounts.objects.all()
    }
    return render(request, template_name='index.html', context=context)


def render_choice(request, reader_id):
    return render(request, template_name='choice.html')


def render_books_active(request):
    context = {
        'books': Book.objects.filter(is_active=True)
    }
    return render(request, template_name='books_active.html', context=context)
