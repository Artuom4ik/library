# Generated by Django 5.0 on 2023-12-10 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=200, verbose_name='Отчество')),
            ],
        ),
    ]
