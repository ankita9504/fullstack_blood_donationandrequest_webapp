from django.urls import path

from django.contrib.auth.views import LoginView
from . import views
from .views import search_blood_view
urlpatterns = [
    path('hospitallogin', LoginView.as_view(template_name='hospital/hospitallogin.html'),name='hospitallogin'),
    path('hospitalsignup', views.hospital_signup_view,name='hospitalsignup'),
    path('search_blood',search_blood_view,name='search_blood'),
    path('hospital-dashboard', views.hospital_dashboard_view,name='hospital-dashboard'),
    path('make-request', views.make_request_view,name='make-request'),
    path('my-request', views.my_request_view,name='my-request'),
]