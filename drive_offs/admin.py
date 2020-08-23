from django.contrib import admin
from django import forms

from .models import DriveOff

# class DriveOffForm(forms.ModelForm):


#     def fields_required(self, fields):
#         """Used for conditionally marking fields as required."""
#         for field in fields:
#             if not self.cleaned_data.get(field, ''):
#                 msg = forms.ValidationError("This field is required.")
#                 self.add_error(field, msg)

#     def clean(self):
#         paid_val = self.cleaned_data.get('paid')
#         if paid_val:
#             self.fields_required(['paid_date'])
#         else:
#             self.cleaned_data['paid_date'] = None
#         return self.cleaned_data


class DriveOffAdmin(admin.ModelAdmin):
    # form = DriveOffForm
    
    list_display = ['date_time', 'reg_no',
        'transaction_amount', 'paid', 'staff_name']
    list_filter = ['date_time']
    search_fields = ['reg_no']
    date_hierarchy = 'date_time'
    fields = ['date_time', 'reg_no', ('paid', 'paid_date'), 'vehicle_type', 'vehicle_make', 'vehicle_colour',
              'transaction_amount', 'staff_name', 'police_reference', 'additional_notes']




admin.site.register(DriveOff, DriveOffAdmin)


