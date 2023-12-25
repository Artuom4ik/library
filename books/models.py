from django.db import models
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=200, verbose_name='Имя')
    last_name = models.CharField(max_length=200, verbose_name='Фамилия')

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class Reader(models.Model):
    first_name = models.CharField(max_length=200, verbose_name='Имя')
    last_name = models.CharField(max_length=200, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=200, verbose_name='Отчество')

    def __str__(self) -> str:
        return self.last_name


class Book(models.Model):
    is_active = models.BooleanField(default=True, verbose_name='Может быть выдана')
    code = models.IntegerField(blank=True, null=True, verbose_name='Код книги')
    title = models.CharField(max_length=200, verbose_name='Название')
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE, 
        related_name='books', 
        verbose_name='Автор')
    
    def __str__(self) -> str:
        return self.title


class Booking(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='bookings', verbose_name='Книга')
    reader = models.ForeignKey(Reader, on_delete=models.PROTECT, related_name='bookings', verbose_name='Читатель')
    taking_at = models.DateTimeField(default=timezone.now(), verbose_name='Дата взятия книги')
    return_at = models.DateTimeField(null=True, blank=True, verbose_name='Дата возврата книги')

    def __str__(self) -> str:
        return f'{self.reader.last_name} {self.reader.first_name} {self.book.code}'