from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, request
from django.views.generic.edit import CreateView
from .forms import ConsumerSignUpForm
from service.models import User, Products

def home(request):
    return render(request,'consumer/home.html')

def user_profile(request):
    return render(request,'consumer/userprofile.html')

#class consumer_register(CreateView):
    # model = User
    # form_class = ConsumerSignUpForm
    # template_name = '../templates/consumer/register.html'

def consumer_register(request):
    if request.method == 'POST':
        form = ConsumerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('consumer-login')
    else:
        form = ConsumerSignUpForm()
    return render(request, 'consumer/register.html', {'form': form})


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('consumer-home')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'consumer/login.html',
    context={'form':AuthenticationForm()})


def productView(request,id):
    product = Products.objects.filter(id=id)

    return render(request, 'consumer/product_view.html',{'product':product[0]})