import requests

from django.core.management.base import BaseCommand

from books.models import Author, Book


class Command(BaseCommand):
    help = 'Adds authors and their books to the database.'

    def add_arguments(self, parser):
        parser.add_argument('--count', '-c', default=100, type=int)

    def handle(self, *args, **options):
        self.add_books(count=options['count'])

    def add_books(self, count):
        url = 'https://mybook.ru/api/books/'
        params = {
            'type': 'text',
            'is_synced': 'true',
            'o': 'popular',
            'limit': count
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        for book in response.json()['objects']:
            book_code = book['id']
            author_first_name = book['main_author']['first_name']
            author_last_name = book['main_author']['last_name']
            title = book['name']
            author, create = Author.objects.get_or_create(first_name=author_first_name, last_name=author_last_name)
            Book.objects.update_or_create(code=book_code, title=title, author=author)