from django.forms import ModelForm
from django import forms

from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Order(ModelForm):
    # class container metadata
    class Meta: 
        model = CustomerOrder()
        #all fields for the form
        fields = "__all__"  

#Inherit from the UserCreationForm, modify the fields we want
class RegisterUserForm(UserCreationForm): 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class GuestChat(forms.Form):
    guest_name = forms.CharField(label='Your name', max_length=100)