from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime
from django.utils import timezone





class DriveOff(models.Model):
    date_time = models.DateTimeField('date and time')
    reg_no = models.CharField('Registration no', max_length=20)
    paid = models.BooleanField("Paid?")
    paid_date = models.DateField('Paid Date',blank=True, null=True)
    vehicle_type = models.CharField(
        'vehicle type (eg: Car)', max_length=50, blank=True)
    vehicle_make = models.CharField(max_length=100, blank=True)
    vehicle_colour = models.CharField(max_length=50, blank=True)
    transaction_amount = models.DecimalField(
        "Transaction amount (£)", max_digits=6, decimal_places=2)
    staff_name = models.CharField(max_length=50)
    police_reference = models.CharField(
        'police reference no:', max_length=20, blank=True)
    additional_notes = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        self.reg_no = self.reg_no.upper()
        super().save(*args, **kwargs)

    # def fields_required(self, fields):
    #     """Used for conditionally marking fields as required."""
    #     for field in fields:
    #         if not self.cleaned_data.get(field, ''):
    #             msg = forms.ValidationError("This field is required.")
    #             self.add_error(field, msg)

    def clean(self):

        now = timezone.now()
        if self.date_time > now:
            raise ValidationError({'date_time': ValidationError('The "Date and Time" cannot be a future Date and Time')})

        if self.paid and not self.paid_date:
            raise ValidationError({'paid_date': ValidationError('If paid enter "Paid Date"')}) 

        if not self.paid and self.paid_date:
            raise ValidationError({'paid_date': ValidationError('Was this Drive off paid? If so tick "Paid". If not Clear "Paid Date"')})       

        if self.paid_date and self.paid_date < self.date_time.date():
            raise ValidationError({'paid_date': ValidationError('The "Paid Date" is before Drive Off Date')})

        if self.paid_date and self.paid_date > now.date():
            raise ValidationError({'paid_date': ValidationError('The "Paid Date" cannot be a future Date')})

        if not self.paid and self.paid_date:
            raise ValidationError({'paid_date': ValidationError('Was this Drive off paid? If so tick "Paid". If not Clear "Paid Date"')})
        
    class Meta:
        ordering = ['-date_time']

    def __str__(self):
        return self.reg_no
