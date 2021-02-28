from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
# import sys
# sys.path.append('..\service')
from service.models import User,Consumer 

class ConsumerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(required=True)
    locality = forms.CharField(required=True)   
    state = forms.CharField(required=True) 
    city = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_consumer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.email = self.cleaned_data.get('email')
        user.address = self.cleaned_data.get('address')
        user.locality = self.cleaned_data.get('locality')
        user.state = self.cleaned_data.get('state')
        user.city = self.cleaned_data.get('city')
        user.save()
        consumer = Consumer.objects.create(user=user)
        consumer.save()
        return user


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    email = forms.EmailField()
    address = forms.CharField()
    locality = forms.CharField()   
    state = forms.CharField() 
    city = forms.CharField()
    class Meta:
        model = Consumer
        fields = ['email', 'first_name','last_name','phone_number','address','locality','state','city']

