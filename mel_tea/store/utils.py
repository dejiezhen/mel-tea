import json
from .models import *


def guestCookieCart(request):
    items = []
    try:
        cookiesCart = json.loads(request.COOKIES["cart"])
    except:
        cookiesCart = {}
    order = {'cart_total':0, 'cart_quantity':0}
    cart_items = order['cart_quantity'] # Currently 0
    for i in cookiesCart:
        try:
            # Adding the total items in cookies cart to cart_items
            cart_items += cookiesCart[i]["quantity"]
            # Getting product itself
            product = BobaProduct.objects.get(id=i)
            # Getting total of each product
            total = (product.price * cookiesCart[i]['quantity'])
            
            # Grabbing cart total and cart quantity and updating their values
            order['cart_total'] += total
            order['cart_quantity'] += cookiesCart[i]["quantity"]

            # Outputting the items into the cart
            boba_items = {
                'product':{
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'image_url': product.image_url
                },
                'quantity': cookiesCart[i]["quantity"],
                'calc_total': total 
                }
    
            items.append(boba_items)
        except: 
            # if item in database gets deleted
            pass
    return {"items": items, "order": order, 'cart_items':cart_items}      

def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        # Get customer order or if complete = false, create new order
        order, created = CustomerOrder.objects.get_or_create(customer=customer)
        # Get all the items attached to the order of the customer. Querying child obj 
        # get OrderItem model with orderitem_set.all(). This order is attached to customer
        items = order.orderitem_set.all()   # (USE ITEM FOR CHILDREN)

        cart_items = order.cart_quantity
    else:
        cookie = guestCookieCart(request)
        cart_items = cookie['cart_items']
        order = cookie['order']
        items = cookie['items']
    return {"items": items, "order": order, 'cart_items':cart_items} 