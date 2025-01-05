# admin.py
from django.contrib import admin
from .models import Account, User, Transaction, Log, BankNetwork, SecurityModule

admin.site.register(Account)
admin.site.register(User)
admin.site.register(Transaction)
admin.site.register(Log)
admin.site.register(BankNetwork)
admin.site.register(SecurityModule)
