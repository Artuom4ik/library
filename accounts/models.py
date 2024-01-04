from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='account', verbose_name='')
    patronymic = models.CharField(max_length=200, verbose_name='Отчество')
    image = models.ImageField(default='', verbose_name='Изображение')
    short_description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.user.last_name} {self.user.first_name}'