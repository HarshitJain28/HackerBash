from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('',views.home,name="consumer-home"),
    path('profile/',views.user_profile,name="consumer-profile"),
    path('products/',views.SearchResultView.as_view(),name='search-product'),
    path('register/',views.consumer_register,name='consumer-register'),
    path('login/',views.login_request,name='consumer-login'),
    path('product_view/<int:id>', views.productView, name="Product_view"),
    path('logout/',auth_views.LogoutView.as_view(template_name='consumer/logout.html'),name="consumer-logout"),
    #path('update_profile/',views.update_profile,name='update-consumer-profile')

    
]
