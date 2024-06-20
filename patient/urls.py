from django.urls import path

from django.contrib.auth.views import LoginView
from . import views
from .views import search_blood_view

urlpatterns = [
    path('patientlogin', LoginView.as_view(template_name='patient/patientlogin.html'),name='patientlogin'),
    path('patientsignup', views.patient_signup_view,name='patientsignup'),
    
    path('patient-dashboard', views.patient_dashboard_view,name='patient-dashboard'),
    path('search_blood',search_blood_view,name='search_blood'),
    path('make-request', views.make_request_view,name='make-request'),
    path('my-request', views.my_request_view,name='my-request'),
]