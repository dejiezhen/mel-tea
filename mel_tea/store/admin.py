from django.contrib import admin
from .models import *

# Register your models here.

# Registering the customer model into admin panel
admin.site.register(Customer)

# Register the Boba Product model into admin panel 
admin.site.register(BobaProduct)

# Register the Customer Order model into admin panel 
admin.site.register(CustomerOrder)