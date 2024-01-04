from django.db import models
from django.utils import timezone

from accounts.models import Account

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=200, verbose_name='Имя')
    last_name = models.CharField(max_length=200, verbose_name='Фамилия')

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    is_active = models.BooleanField(default=True, verbose_name='Может быть выдана')
    code = models.IntegerField(blank=True, null=True, verbose_name='Код книги')
    title = models.CharField(max_length=200, verbose_name='Название')
    image = models.ImageField(default='https://www.hachettebookgroup.com/wp-content/uploads/2017/07/missingbook.png', verbose_name='Изображение')
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE, 
        related_name='books', 
        verbose_name='Автор')
    
    def __str__(self) -> str:
        return self.title


class Booking(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='bookings', verbose_name='Книга')
    reader = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='bookings', verbose_name='Читатель')
    taking_at = models.DateTimeField(default=timezone.now(), verbose_name='Дата взятия книги')
    return_at = models.DateTimeField(null=True, blank=True, verbose_name='Дата возврата книги')

    def __str__(self) -> str:
        return f'{self.reader.user.last_name} {self.reader.user.first_name} {self.book.code}'