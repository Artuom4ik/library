from django import forms


class RegistrationForms(forms.Form):
    username = forms.CharField(max_length=200, label='Никнейм')
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите пароль'
        }),
        label='Пароль')
    first_name = forms.CharField(max_length=200, label='Имя')
    last_name = forms.CharField(max_length=200, label='Фамилия')
    patronymic = forms.CharField(max_length=200, label='Отчество', required=False)


class LoginForms(forms.Form):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    