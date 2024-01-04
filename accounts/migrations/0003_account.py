# Generated by Django 3.2.22 on 2024-01-04 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_accounts_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patronymic', models.CharField(max_length=200, verbose_name='Отчество')),
                ('image', models.ImageField(default='', upload_to='', verbose_name='Изображение')),
                ('short_description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
