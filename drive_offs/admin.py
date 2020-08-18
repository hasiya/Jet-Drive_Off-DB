from django.contrib import admin

from .models import DriveOff

class DriveOffAdmin(admin.ModelAdmin):
    list_display = ['date_time', 'reg_no','transaction_amount']
    list_filter = ['date_time']
    search_fields = ['reg_no']

admin.site.register(DriveOff,DriveOffAdmin);
