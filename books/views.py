from django.shortcuts import render

from .models import Book, Reader, Author
# Create your views here.

def readers(request):
    context = {
        'readers': Reader.objects.all()
    }
    return render(request, template_name='readers.html', context=context)


def render_choice(request):
    return render(request, template_name='choice.html')


def render_books_active(request):
    context = {
        'books': Book.objects.filter(is_active=True)
    }
    return render(request, template_name='books_active.html', context=context)
