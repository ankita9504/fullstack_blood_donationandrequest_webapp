
from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum,Q
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from django.core.mail import send_mail
from django.contrib.auth.models import User
from blood import forms as bforms
from blood import models as bmodels
from donor.models import Donor as dmodels 

def hospital_signup_view(request):
    userForm=forms.HospitalUserForm()
    hospitalForm=forms.HospitalForm()
    mydict={'userForm':userForm,'hospitalForm':hospitalForm}
    if request.method=='POST':
        userForm=forms.HospitalUserForm(request.POST)
        hospitalForm=forms.HospitalForm(request.POST,request.FILES)
        if userForm.is_valid() and hospitalForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            hospital=hospitalForm.save(commit=False)
            hospital.user=user
            # hospital.bloodgroup=hospitalForm.cleaned_data['bloodgroup']
            hospital.save()
            my_hospital_group = Group.objects.get_or_create(name='HOSPITAL')
            my_hospital_group[0].user_set.add(user)
        return HttpResponseRedirect('hospitallogin')
    return render(request,'hospital/hospitalsignup.html',context=mydict)

def hospital_dashboard_view(request):
    hospital= models.Hospital.objects.get(user_id=request.user.id)
    dict={
        'requestpending': bmodels.BloodRequest.objects.all().filter(request_by_hospital_id=hospital).filter(status='Pending').count(),
        'requestapproved': bmodels.BloodRequest.objects.all().filter(request_by_hospital_id=hospital).filter(status='Approved').count(),
        'requestmade': bmodels.BloodRequest.objects.all().filter(request_by_hospital_id=hospital).count(),
        'requestrejected': bmodels.BloodRequest.objects.all().filter(request_by_hospital_id=hospital).filter(status='Rejected').count(),
    }
   
    return render(request,'hospital/hospital_dashboard.html',context=dict)

def make_request_view(request):
    request_form=bforms.RequestForm()
    if request.method=='POST':
        request_form=bforms.RequestForm(request.POST)
        if request_form.is_valid():
            blood_request=request_form.save(commit=False)
            blood_request.bloodgroup=request_form.cleaned_data['bloodgroup']
            hospital= models.Hospital.objects.get(user_id=request.user.id)
            blood_request.request_by_hospital=hospital
            blood_request.save()
            return HttpResponseRedirect('my-request')  
    return render(request,'hospital/makerequest.html',{'request_form':request_form})

def my_request_view(request):
    hospital= models.Hospital.objects.get(user_id=request.user.id)
    blood_request=bmodels.BloodRequest.objects.all().filter(request_by_hospital=hospital)
    return render(request,'hospital/my_request.html',{'blood_request':blood_request})
def search_blood_view(request):
    if request.method=='POST':
        bloodgroup=request.POST.get('bloodgroup',None)
        address=request.POST.get('address',None)    
        if bloodgroup and address:
            donors=dmodels.objects.all().filter(bloodgroup=bloodgroup,address__icontains=address)
            return render(request,'hospital/search_blood.html',{'donors':donors,'bloodgroup':bloodgroup,'address':address})
    return render(request,'hospital/searchform.html')