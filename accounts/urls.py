from django.urls import path, include
from django.shortcuts import redirect

from . import views

app_name = "accounts"

urlpatterns = [
    path('registration/', views.registration),
]