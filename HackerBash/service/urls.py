from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.service_profile,name="service-profile"),
    path('register/',views.service_register,name="service-register"),
    path('login/',auth_views.LoginView.as_view(template_name='service/login.html'),name="service-login")
    
]