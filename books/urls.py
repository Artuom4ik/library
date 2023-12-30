from django.urls import path, include
from django.shortcuts import redirect

from . import views

app_name = "books"

urlpatterns = [
    path('choice/<int:reader_id>/', views.render_choice),
    path('choice/<int:reader_id>/active_books/', views.render_books_active, name='active-books'),
    path('choice/<int:reader_id>/active_books/take_book/<int:book_id>/', views.take_book),
    path('choice/<int:reader_id>/return_book/', views.render_return_book),
    path('choice/<int:reader_id>/return_book/<int:book_id>/', views.return_book)
]