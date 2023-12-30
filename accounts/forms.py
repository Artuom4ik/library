from django import forms


class AccountForms(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    patronymic = forms.CharField(max_length=200, required=False)
    