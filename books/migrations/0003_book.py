# Generated by Django 5.0 on 2023-12-10 15:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_reader'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Может быть выдана')),
                ('code', models.IntegerField(blank=True, null=True, verbose_name='Код книги')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='books.author', verbose_name='Автор')),
                ('reader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to='books.reader', verbose_name='Читатель')),
            ],
        ),
    ]
