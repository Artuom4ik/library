from django.urls import path, include
from django.shortcuts import redirect

from . import views

app_name = "books"

urlpatterns = [
    path('choice/', views.render_choice),
    path('active_books/', views.render_books_active),
]