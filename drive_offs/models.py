from django.db import models


class DriveOff(models.Model):
    date_time = models.DateTimeField('date and time')
    reg_no = models.CharField('Registration no', max_length=20)
    paid = models.BooleanField("Paid?")
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

    class Meta:
        ordering = ['-date_time']

    def __str__(self):
        return self.reg_no
