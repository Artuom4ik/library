from django.urls import path

from .views import RegistrationFormView, LoginFormView, logout_view

app_name = "accounts"

urlpatterns = [
    path('registration/', RegistrationFormView.as_view(), name='registration'),
    path('authentication/', LoginFormView.as_view(), name='login'),
    path('logout/', logout_view, name='logout')
]