# Source: https://docs.djangoproject.com/en/3.2/topics/auth/default/

#Query set doc: https://docs.djangoproject.com/en/3.2/ref/models/querysets/
#Django Relationship Models: https://www.webforefront.com/django/setuprelationshipsdjangomodels.html

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

#Creating our views with model and forms
from .models import *
from .forms import RegisterUserForm

# Functions to direct you towards the correct html path

def store(request):
    context = {}
    return render(request, 'store/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        # Get customer order or if complete = false, create new order
        order, created = CustomerOrder.objects.get_or_create(customer=customer)

        # Get all the items attached to the order of the customer. Querying child obj 
        # get OrderItem model with orderitem_set.all(). This order is attached to customer
        items = order.orderitem_set.all()   # (USE ITEM FOR CHILDREN)
    else:
        # Maybe make the users create the account?
        items = []
        order = {'cart_total':0, 'cart_quantity':0}

    context = {"items": items, "order": order}
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        # Get customer order or if complete = false, create new order
        order, created = CustomerOrder.objects.get_or_create(customer=customer)

        # Get all the items attached to the order of the customer. Querying child obj 
        # get OrderItem model with orderitem_set.all(). This order is attached to customer
        items = order.orderitem_set.all()   # (USE ITEM FOR CHILDREN)
    else:
        # Maybe make the users create the account?
        items = []
        order = {'cart_total':0, 'cart_quantity':0}
    context = {"items":items, "order":order}
    return render(request, 'store/checkout.html', context)

def simulate(request):
    context = {}
    return render(request, 'store/simulate.html', context)

def about(request): 
    context = {}
    return render(request, 'store/about.html', context)

def menu(request): 
    # Get all our object
    products = BobaProduct.objects.all()
    # Dictionary to hold our products
    context = {"products": products}
    return render(request, 'store/menu.html', context)

def loginUser(request): 
    # If logged in, won't be able to acces /register path
    # user redirected back to home store page
    if request.user.is_authenticated:
        return redirect('store')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None: 
                login(request, user)
                print(username + " has logged in")
                return redirect('store')
            else: 
                # If user enters wrong credentials, send error message
                messages.info(request, 'Your Username or Password is Incorrect')

    context = {}
    return render(request, 'store/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def register(request): 
    # If logged in, won't be able to acces /register path
    # user redirected back to home store page
    if request.user.is_authenticated:
        return redirect('store')
    else:
        form = RegisterUserForm()
        if request.method == 'POST':
            form = RegisterUserForm(request.POST)
            if form.is_valid(): #if form is valid, save the form
                form.save()
                # clean our form and only get the username
                username = form.cleaned_data.get('username')
                messages.success(request, "Hello {0}, you have successful registered for an account".format(username))
                return redirect('login') #redirect user to login page is the form is valid
    context = {'form': form}
    return render(request, 'store/register.html', context)

def chatbox(request):
    context = {}
    return render(request, 'store/chatbox.html', context)