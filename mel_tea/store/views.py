"""
views.py

Functions to direct you towards the correct HTML Path. Also the logic to 
build out our website

"""

from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import JsonResponse
from .utils import *
import json

#Creating our views with model and forms
from .models import *
from .forms import GuestChat, RegisterUserForm


def store(request):
    """
    store
    Main Page
    
    Args: 
        request

    """
    cart = cartData(request)
    cart_items = cart['cart_items']
    # order = cart['order']
    # items = cart['items']
    
    # Get all our objects
    products = BobaProduct.objects.all()
    # Dictionary to hold our products
    context = {"products": products, "cart_items": cart_items}
    return render(request, 'store/store.html', context)

def cart(request):
    """
    cart
    Cart Logic
    
    Args: 
        request

    """
    cart = cartData(request)
    cart_items = cart['cart_items']
    order = cart['order']
    items = cart['items']
    # products = BobaProduct.objects.all()
    context = {"items": items, "order": order, 'cart_items':cart_items}
    return render(request, 'store/cart.html', context)

def checkout(request):
    """
    checkout
    checkout Logic. 
    
    Args: 
        request

    """
    cart = cartData(request)
    cart_items = cart['cart_items']
    order = cart['order']
    items = cart['items']
    context = {"items":items, "order":order, 'cart_items':cart_items}
    return render(request, 'store/checkout.html', context)


def about(request): 
    """
    about
    about page - not fully designed
    
    Args: 
        request

    """
    context = {}
    return render(request, 'store/about.html', context)

def menu(request): 
    """
    menu
    menu page logic. displaying all the products in our DB
    
    Args: 
        request

    """
    cart = cartData(request)
    cart_items = cart['cart_items']
    # order = cart['order']
    # items = cart['items']
    # Get all our object
    products = BobaProduct.objects.all()
    # Dictionary to hold our products
    context = {"products": products, "cart_items": cart_items}
    return render(request, 'store/menu.html', context)

# Get Json response when item is added. Put message into template
def updateItem(request):
    """
    updateItem
    
    When users click on the up or down arrow, 
    the item quantity updates
    
    Args: 
        request

    """
    # Getting the data when you add to cart. Body of JSON
    data = json.loads(request.body)
    # Getting values we sent to body as JSON. prodID and Action
    productId = data['prodId']
    action = data['action']

    # Get curr customer
    customer = request.user.customer
    product = BobaProduct.objects.get(id=productId)

    # get order associated with customer
    order, created = CustomerOrder.objects.get_or_create(customer=customer)

    # Get value of curr order. If it exist, want to just change it
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1
    orderItem.save() #saving this order item

    # If the quantity of the order goes below 1, delete the orderItem

    if orderItem.quantity < 1:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)

def loginUser(request): 
    """
    login
    Checks if user is logged in. authenticating the username
    and password with our DB
    
    Args: 
        request

    """

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
    """
    Logout
    Users logging out logic
    
    Args: 
        request

    """
    logout(request)
    return redirect('login')

def register(request): 
    """
    register
    Users can register an account. When users finish registering,
    it will send a signal (signal.py) and save the information to the
    Customer model also. The customer model will be added to the Group 
    model designed for customers. 

    Customer group have limited access. 
    
    Args: 
        request

    """

    # If logged in, won't be able to acces /register path
    # user redirected back to home store page
    if request.user.is_authenticated:
        return redirect('store')
    else:
        form = RegisterUserForm()
        if request.method == 'POST':
            form = RegisterUserForm(request.POST)
            if form.is_valid(): #if form is valid, save the form
                user = form.save()
                # clean our form and only get the username
                username = form.cleaned_data.get('username')
                messages.success(request, "Hello {0}, you have successful registered for an account".format(username))
                return redirect('login') #redirect user to login page is the form is valid
    context = {'form': form}
    return render(request, 'store/register.html', context)

def guestChat(request):
    """
    guestChat
    If the user is not authenticated, they will be redirected to this
    site where they can input a guest name and enter the chatbox
    
    Args: 
        request

    """
    form = GuestChat()
    if request.method == "POST":
        form = GuestChat(request.POST)
        if form.is_valid():
            guestName = form.cleaned_data.get('guest_name')
            return render(request, 'chat/room.html', {"guestName": guestName})
            
    context = {"form": form}   
    return render(request, 'chat/guestUser.html', context)

def room(request):
    """
    room
    Room where users can chat with each other!
    
    Args: 
        request

    """
    cart = cartData(request)
    cart_items = cart['cart_items']
    # order = cart['order']
    # items = cart['items']
 
    # Get all our object
    products = BobaProduct.objects.all()
    # Dictionary to hold our products
    context = {"products": products, "cart_items": cart_items}

    return render(request, 'chat/room.html', context)