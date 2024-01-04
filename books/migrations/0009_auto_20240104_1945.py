# Generated by Django 3.2.22 on 2024-01-04 16:45

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_account'),
        ('books', '0008_alter_booking_taking_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='reader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bookings', to='accounts.account', verbose_name='Читатель'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='taking_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 16, 45, 49, 586811, tzinfo=utc), verbose_name='Дата взятия книги'),
        ),
    ]
