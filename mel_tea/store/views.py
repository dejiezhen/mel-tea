from django.shortcuts import render

# Functions to direct you towards the correct html path

def store(request):
    context = {}
    return render(request, 'store/store.html', context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

def simulate(request):
    context = {}
    return render(request, 'store/simulate.html', context)

def about(request): 
    context = {}
    return render(request, 'store/about.html', context)

def menu(request): 
    context = {}
    return render(request, 'store/menu.html', context)