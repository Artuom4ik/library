from django.urls import path, include
from django.shortcuts import redirect

from . import views

app_name = "books"

urlpatterns = [
    path('', views.render_choice, name='choice'),
    path('active_books/', views.render_books_active, name='active-books'),
    path('take_book/<int:book_id>/', views.take_book, name='take-book'),
    path('return_book/', views.render_return_book),
    path('return_book/<int:book_id>/', views.return_book)
]