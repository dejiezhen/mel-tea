# Source:https://docs.djangoproject.com/en/3.2/topics/files/ 

from django.db import models

# Create your models here.

# Connection with our database. 
# Running python3 manage.py makemigrations - implement each model into database
# python3 manage.py migration to apply the migrations

# Customer Model
class Customer(models.Model): 
    # null = True will allow us to make changes to database. 
    # 2 possible vals for no data, NULL or empty string
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    # Record whe nthe customer was created 
    date_created = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name

# Boba Product Model
class BobaProduct(models.Model):
    WITH_BOBA = [
        ('YES', 'Boba'),
        ('NO', 'No Boba')
    ]
    name = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices= WITH_BOBA)
    image = models.ImageField(upload_to='boba')
    description = models.CharField(max_length=500, null=True)
    date_created = models.DateTimeField(auto_now_add=True) 

# Customer's Order model. Addresses the current status of delivery and what toppings
class CustomerOrder(models.Model):
    CURR_STATUS = [
        ("Pending", "Pending"),
        ("Delivering", "Delivering"),
        ("Delivered", "Delivered")
    ]

    WITH_BOBA = [
        ('YES', 'Boba'),
        ('NO', 'No Boba')
    ]
    #customer
    #product
    date_created = models.DateTimeField(auto_now_add=True) 
    toppings = models.CharField(max_length=200, null=True, choices= WITH_BOBA)
    status = models.CharField(max_length=200, null=True, choices=CURR_STATUS)

