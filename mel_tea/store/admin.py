from django.contrib import admin
from .models import *

# Register your models here.

# Registering the Customer model into admin panel
admin.site.register(Customer)

# Register the Boba Product model into admin panel 
admin.site.register(BobaProduct)

# Register the Customer Order model into admin panel 
admin.site.register(CustomerOrder)

# Register the Order Item model into admin panel
admin.site.register(OrderItem)

# Register the Customer Shipping Address model into admin panel
admin.site.register(CustomerShippingAddresses)