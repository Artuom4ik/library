from django.urls import path, include
from django.shortcuts import redirect

from .views import MyFormView

app_name = "accounts"

urlpatterns = [
    path('registration/', MyFormView.as_view()),
]