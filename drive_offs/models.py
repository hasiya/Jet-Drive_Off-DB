from django.db import models

class DriveOff(models.Model):
    date_time = models.DateTimeField('date and time')
    reg_no = models.CharField('Registration no',max_length=20)
    vehicle_type = models.CharField('vehicle type (eg: Car)',max_length=50,blank=True)
    vehicle_make = models.CharField(max_length=100,blank=True)
    vehicle_colour = models.CharField(max_length=50,blank=True)
    transaction_amount = models.DecimalField("Transaction Amount (£)",max_digits=6, decimal_places=2)
    staff_name = models.CharField(max_length=50)
    additional_notes = models.TextField(blank=True)

    class Meta:
        ordering = ['date_time']
        
    def __str__(self):
        return self.reg_no

