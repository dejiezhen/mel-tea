from django.forms import ModelForm
from django import forms

from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Order(ModelForm):
    """
    Order Form

    Args: 
        ModelForm

    """
    class Meta: 
        model = CustomerOrder()
        #all fields for the form
        fields = "__all__"  

class RegisterUserForm(UserCreationForm): 
    """
    RegisterUser Form

    Inherits from the UserCreationForm and modify the fields we want
    Args: 
        UserCreationForm - inherits from UserCreationForm

    """
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class GuestChat(forms.Form):
    """
    GuestChat Form

    Form for Guest to enter their name to go into the chat room
    
    Args: 
        forms.Form

    """
    guest_name = forms.CharField(label='Your name', max_length=100)