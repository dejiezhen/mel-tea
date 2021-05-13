# Source:https://docs.djangoproject.com/en/3.2/topics/files/ 
# Source2: https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_one/

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Connection with our database. 
# Running python3 manage.py makemigrations - implement each model into database
# python3 manage.py migrate to apply the migrations

# Customer Model
class Customer(models.Model): 
    # null = True will allow us to make changes to database. 
    # 2 possible vals for no data, NULL or empty string
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    # Record whe nthe customer was created 
    date_created = models.DateTimeField(auto_now_add=True) 

    # Return name. This is the name for the product query
    def __str__(self):
        return self.name

# Boba Product Model
class BobaProduct(models.Model):
    WITH_BOBA = [
        ('YES', 'Boba'),
        ('NO', 'No Boba')
    ]
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices= WITH_BOBA)
    image = models.ImageField(upload_to='boba', default="{% static 'images/filler.jpg' %}", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name

    # Incase the image is empty. 
    # Change product.image.url to ''
    @property #@property allow us to access as an attribute
    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

# Customer's Order model. Addresses the current status of delivery and what toppings
class CustomerOrder(models.Model):
    # CURR_STATUS = [
    #     ("Pending", "Pending"),
    #     ("Delivering", "Delivering"),
    #     ("Delivered", "Delivered")
    # ]

    # WITH_BOBA = [
    #     ('YES', 'Boba'),
    #     ('NO', 'No Boba')
    # ]

    # Customer can have multiple orders. Many orders to one user = ForeignKey
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True) 
    # toppings = models.CharField(max_length=200, null=True, choices= WITH_BOBA)
    # status = models.CharField(max_length=200, null=True, choices=CURR_STATUS)
    completion = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property 
    # Getting the sum of all products
    def cart_total(self):
        order_items = self.orderitem_set.all()
        # Getting the sum of every order by the customer
        total = sum([item.calc_total for item in order_items])
        return total

    @property
    # Getting total amount of items (quantity)
    def cart_quantity(self):
        order_items = self.orderitem_set.all()
        total = sum([item.quantity for item in order_items])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(BobaProduct, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(CustomerOrder, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.order)

    @property
    def calc_total(self):
        total = self.product.price * self.quantity
        return total

class CustomerShippingAddresses(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(CustomerOrder, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.address

