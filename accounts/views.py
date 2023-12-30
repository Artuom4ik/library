from django.shortcuts import render, redirect
from django.views import View

from .forms import AccountForms
from .models import Accounts


class MyFormView(View):
    form_class = AccountForms
    initial = {'key': 'value'}
    template_name = 'registration.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            patronymic = form.cleaned_data.get('patronymic')
            Accounts.objects.update_or_create(
                first_name=first_name,
                last_name=last_name,
                patronymic=patronymic
            )
            return redirect('index')

        return render(request, self.template_name, {'form': form})
