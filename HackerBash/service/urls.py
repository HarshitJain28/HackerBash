from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.user_profile,name="service-profile"),
    path('register/',views.service_register,name="service-register"),
    path('login_service/',views.login_request,name="service-login"),
    path('product/new',views.ProductCreateView.as_view(),name='new-product'),
    path('logout/',auth_views.LogoutView.as_view(template_name='service/logout_service.html'),name="service-logout"),
    
]