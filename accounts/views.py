from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .forms import RegistrationForms, LoginForms
from .models import Accounts


class RegistrationFormView(View):
    form_class = RegistrationForms
    initial = {'key': 'value'}
    template_name = 'registration.html'

    def get(self, request, *args, **kwargs):
        form = RegistrationForms()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegistrationForms(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            patronymic = form.cleaned_data.get('patronymic')

            Accounts.objects.get_or_create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                patronymic=patronymic
            )

            User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name)
            
            return redirect('index')

        return render(request, self.template_name, {'form': form})
    

class LoginFormView(View):
    form_class = LoginForms
    initial = {'key': 'value'}
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        form = LoginForms()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForms(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user and user.is_active:
                login(request, user)
                return redirect('books:choice')
            
            return redirect('index')

        return render(request, self.template_name, {'form': form})


def logout_view(request):
    logout(request)

    return redirect('index')
