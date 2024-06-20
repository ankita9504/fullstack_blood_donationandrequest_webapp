from django import forms

from . import models


class BloodForm(forms.ModelForm):
    class Meta:
        model=models.Stock
        fields=['bloodgroup','unit']

class RequestForm(forms.ModelForm):
    class Meta:
        model=models.BloodRequest
        fields=['patient_name','patient_age','reason','bloodgroup','unit']



class DonationCampForm(forms.ModelForm):
    class Meta:
        model = models.DonationCamp
        fields = ['camp_name', 'camp_venue', 'address', 'pincode', 'organizer', 'contact_number', 'date', 'starttime', 'endtime']