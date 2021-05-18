from django.db.models.signals import post_save
from django.contrib.auth.models import Group, User
from .models import Customer, CustomerOrder

def customer_profile(sender, instance, created, **kwargs):
	"""
    customer_profile
    When users register for an account, they will be added
	to the "customer" group and added to the Customer Model
    
    Args: 
        request

    """
	if created:
		group = Group.objects.get(name='customer')
		instance.groups.add(group)
		Customer.objects.create(
			user=instance,
			name=instance.username,
			)
		print('Profile created!')

post_save.connect(customer_profile, sender=User)