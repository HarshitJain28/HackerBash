from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, request
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .forms import ConsumerSignUpForm
from .forms import UserUpdateForm
from django.db.models import Q
from service.models import User, Products, Consumer

@login_required
def home(request):
	if request.user.is_consumer:
		products = Products.objects.all()
		return render(request,'consumer/home.html',{'products':products})
	else:
		messages.error(request,"Does Not Belong To Consumer")
		return redirect('consumer-login')

# @login_required
# def user_profile(request):
#     consumer = request.user

#     return render(request,'consumer/userprofile.html',{'consumer':consumer})


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
	if request.user.is_consumer:
		product = Products.objects.filter(id=id)
		return render(request, 'consumer/product_view.html',{'product':product[0]})
	else:
		messages.error(request,"Does Not Belong To Consumer")
		return redirect('consumer-login')


@login_required
def user_profile(request):
	if request.user.is_consumer:
		if request.method == 'POST':
			u_form = UserUpdateForm(request.POST, instance=request.user)
			if u_form.is_valid():
				u_form.save()
				messages.success(request, f'Your profile has been updated')
				return redirect('consumer-profile')
		else:
			u_form = UserUpdateForm(instance=request.user)
		context = {
			'u_form': u_form,
			'consumer': request.user
		}
		return render(request, 'consumer/userprofile.html',context)
	else:
		messages.error(request,"Does Not Belong To Consumer")
		return redirect('consumer-login')

class SearchResultView(ListView):
	model = Products
	context_object_name = 'products'
	template_name = 'consumer/searchProducts.html'
	
	def get_queryset(self):
		if request.user.is_consumer:
			query = self.request.GET.get('q')
			products = Products.objects.filter(product_name__icontains = query)
			return products
		else:
			messages.error(request,"Does Not Belong To Consumer")
			return redirect('consumer-login')