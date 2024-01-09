import json
import os.path

import requests

from django.core.management.base import BaseCommand

from books.models import Author, Book


class Command(BaseCommand):
    help = 'Adds authors and their books to the database.'

    def add_arguments(self, parser):
        parser.add_argument('--count', '-c', default=100, type=int)
        parser.add_argument('--json_path', '-path')

    def handle(self, *args, **options):
        if options['json_path']:
            self.add_book(json_path=options['json_path'])
        else:
            self.add_books(count=options['count'])
    
    def add_book(self, json_path):
        with open(json_path, 'r', encoding='UTF8') as file:
            json_path = json.load(file)

        for book in json_path:
            self.add_books(count=0, book=book)

    def add_books(self, count, book=''):
        if count and not book:
            url = 'https://mybook.ru/api/books/'
            params = {
                'type': 'text',
                'is_synced': 'true',
                'o': 'popular',
                'limit': count
            }
            response = requests.get(url, params=params)
            response.raise_for_status()
            book_json = response.json()['objects']
            for book in book_json:
                book_code = book['id']
                author_first_name = book['main_author']['first_name']
                author_last_name = book['main_author']['last_name']
                title = book['name']
                author, create = Author.objects.get_or_create(first_name=author_first_name, last_name=author_last_name)
                Book.objects.update_or_create(code=book_code, title=title, author=author)
        
        else:
            author_first_name = book['first_name']
            author_last_name = book['last_name']
            title = book['title']
            book_code = book['code']
            image = book['image']
            author, create = Author.objects.get_or_create(first_name=author_first_name, last_name=author_last_name)
            Book.objects.update_or_create(code=book_code, title=title, image=image, author=author)
