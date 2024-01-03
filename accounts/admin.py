from django.contrib import admin

from .models import Accounts
# Register your models here.

@admin.register(Accounts)
class AccountsAdmin(admin.ModelAdmin):
    pass