from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="consumer-home"),
    path('profile/',views.user_profile,name="consumer-profile"),
    path('register/',views.consumer_register,name='consumer-register'),
    path('login/',views.login_request,name='consumer-login'),
    path('productView/<int:id>', views.productView, name="ProductView"),
    
]
