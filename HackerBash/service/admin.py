from django.contrib import admin
from .models import ServiceProvider,User,Consumer, Products


admin.site.register(ServiceProvider)
admin.site.register(Consumer)
admin.site.register(User)
admin.site.register(Products)


