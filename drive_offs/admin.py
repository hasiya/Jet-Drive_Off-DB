from django.contrib import admin

from .models import DriveOff


class DriveOffAdmin(admin.ModelAdmin):
    list_display = ['date_time', 'reg_no', 'transaction_amount', 'paid','staff_name']
    list_filter = ['date_time']
    search_fields = ['reg_no']
    date_hierarchy = 'date_time'
    fields = ['date_time', ('reg_no','paid'), 'vehicle_type', 'vehicle_make', 'vehicle_colour',
              'transaction_amount', 'staff_name', 'police_reference', 'additional_notes']

admin.site.register(DriveOff, DriveOffAdmin)
