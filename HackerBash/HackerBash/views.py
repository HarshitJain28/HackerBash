from django.shortcuts import render
from django.http import HttpResponseRedirect, request



def landing(request):
    return render(request,'consumer/landing.html')

def contact(request):
    return render(request,'consumer/contact.html')
