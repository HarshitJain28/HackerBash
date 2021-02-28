from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, request
from django.views.generic import CreateView
from .forms import ServiceProviderSignUpForm, UserUpdateForm
from .models import ServiceProvider, User, Products
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

# def service_profile(request):
#     context = {"service":ServiceProvider.objects.all()}
#     return render(request,'service/serviceprofile.html',context)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Products
    fields = ['product_name', 'product_desc','product_price']
    
    def form_valid(self, form):
        if request.user.is_serviceProvider:
            obj = ServiceProvider.objects.filter(user=self.request.user)
            company_name = obj[0]
            form.instance.product_distributer = company_name
            return super().form_valid(form)
        else:
            messages.error(request,"Does Not Belong To ServiceProvider")
            return redirect('service-login')


def service_register(request):
    if request.method == 'POST':
        form = ServiceProviderSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('service-login')
    else:
        form = ServiceProviderSignUpForm()
    return render(request, 'service/register.html', {'form': form})


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('service-profile')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'service/login_service.html',
    context={'form':AuthenticationForm()})



@login_required
def user_profile(request):
    if request.user.is_serviceProvider:
        if request.method == 'POST':
            u_form = UserUpdateForm(request.POST, instance=request.user)
            if u_form.is_valid():
                u_form.save()
                messages.success(request, f'Your profile has been updated')
                return redirect('service-profile')
        else:
            u_form = UserUpdateForm(instance=request.user)
        context = {
            'u_form': u_form,
            'serviceProvider': request.user
        }
        return render(request, 'service/serviceprofile.html',context)
    else:
        messages.error(request,"Does Not Belong To ServiceProvider")
        return redirect('service-login')


