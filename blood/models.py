from django.db import models
from patient import models as pmodels
from donor import models as dmodels
from hospital import models as hmodels

class contact(models.Model):
   name=models.CharField(max_length=25)
   email=models.EmailField()
   message=models.CharField(max_length=100)
class Stock(models.Model):
    bloodgroup=models.CharField(
        max_length=10
    )
    unit=models.PositiveIntegerField(
        default=0
    )
    def __str__(self):
        return self.bloodgroup

class BloodRequest(models.Model):
    request_by_patient = models.ForeignKey(
        pmodels.Patient,
        null=True,
        on_delete = models.CASCADE
    )
    request_by_hospital = models.ForeignKey(
        hmodels.Hospital,
        null=True,
        on_delete = models.CASCADE
    )
    request_by_donor = models.ForeignKey(
        dmodels.Donor,
        null = True,
        on_delete = models.CASCADE
    )
    patient_name = models.CharField(
        max_length=30
    )
    patient_age = models.PositiveIntegerField()
    reason = models.CharField(
        max_length=500
    )
    bloodgroup = models.CharField(
        max_length=10
    )
    unit = models.PositiveIntegerField(
        default=0
    )
    status = models.CharField(
        max_length=20,
        default="Pending"
    )
    date = models.DateField(
        auto_now=True
    )
    def __str__(self):
        return self.bloodgroup
    
class DonationCamp(models.Model):
    camp_name = models.CharField(
        max_length=50,
        null=True
    )
    camp_venue = models.CharField(
        max_length=50,
        null=True
    )
    address = models.CharField(
        max_length=50,
        null=True
    )
    pincode = models.CharField(
        max_length=50,
        null=True
    )
    organizer = models.CharField(
        max_length=50,
        null=True
    )
    contact_number = models.CharField(
        max_length=50,
        null=True
    )
    date = models.CharField(
        max_length=50,
        null=True
    )
    starttime = models.CharField(
        max_length=50,
        null=True
    )
    endtime = models.CharField(
        max_length=50,
        null=True
    )