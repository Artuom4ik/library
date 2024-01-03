from django.db import models


class Accounts(models.Model):
    username = models.CharField(max_length=200, verbose_name='Никнейм', null=True)
    first_name = models.CharField(max_length=200, verbose_name='Имя')
    last_name = models.CharField(max_length=200, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=200, verbose_name='Отчество')

    def __str__(self) -> str:
        return f'{self.last_name} {self.first_name}'