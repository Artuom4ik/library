# Generated by Django 3.2.22 on 2024-01-09 20:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_auto_20240104_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='short_description',
            field=models.TextField(blank=True, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='account',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='account', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
