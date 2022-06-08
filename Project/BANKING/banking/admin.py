from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ("name","email","phone","id_no")
    
class AccountAdmin(admin.ModelAdmin):
    list_display = ("name","number","balance","type","user","last_transaction")
    list_filter=('type','type')

class AccountTransaction(admin.ModelAdmin):
      list_display = ("type",'amount','transaction','time')
      list_filter=('type','type')

admin.site.register(User,UserAdmin)
admin.site.register(Account,AccountAdmin)
admin.site.register(Transactions,AccountTransaction)