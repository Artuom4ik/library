from django.shortcuts import render

from .models import Book, Reader, Author
# Create your views here.

def index(request):
    context = {
        'readers': Reader.objects.all()
    }
    return render(request, template_name='index.html', context=context)


def registration(request):
    return render(request, template_name='')


def render_choice(request):
    return render(request, template_name='choice.html')


def render_books_active(request):
    context = {
        'books': Book.objects.filter(is_active=True)
    }
    return render(request, template_name='books_active.html', context=context)
