from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, request
from django.views.generic import CreateView
from .forms import ServiceProviderSignUpForm
from .models import ServiceProvider, User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
@login_required
def service_profile(request):
    context = {"service":ServiceProvider.objects.all()}
    return render(request,'service/serviceprofile.html',context)


def service_register(request):
    if request.method == 'POST':
        form = ServiceProviderSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('service-profile')
    else:
        form = ServiceProviderSignUpForm()
    return render(request, 'service/register.html', {'form': form})


# def login_request(request):
#     if request.method=='POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None :
#                 login(request,user)
#                 return redirect('service-profile')
#             else:
#                 messages.error(request,"Invalid username or password")
#         else:
#                 messages.error(request,"Invalid username or password")
#     return render(request, 'service/login.html',context={'form':AuthenticationForm()})
    


