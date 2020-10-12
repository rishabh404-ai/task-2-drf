from django.contrib import admin
from .models import UserRegister,UserRecord


class UserRegisterAdmin(admin.ModelAdmin):
    list_display = ('name','idcard_no','id_type','address','phone_no','email','meet_with',)
    list_filter = ('name','idcard_no','id_type','address','phone_no','email','meet_with',)
    search_fields = ('name','idcard_no','id_type','address','phone_no','email','meet_with',)

admin.site.register(UserRegister,UserRegisterAdmin)    




class UserRecordAdmin(admin.ModelAdmin):
    list_display = ('person','entry_time','exit_time',)
    list_filter = ('person','entry_time','exit_time',)
    search_fields = ('person','entry_time','exit_time',)

admin.site.register(UserRecord,UserRecordAdmin)