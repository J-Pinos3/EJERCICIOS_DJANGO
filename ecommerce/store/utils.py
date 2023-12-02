import json
from .models import *

def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    #cart = json.loads(request.COOKIES.get('cart', '[]'))
    print('Cart from cookies: ', cart)
    items=[]
    #if user is not authenticated the code above will throw an error
    order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
    cartItems = order['get_cart_items']

    for k in cart: #where k is the key of the dictionary (productId)
        try:
            cartItems += cart[k]['quantity']

            product = Product.objects.get(id=k)
            total = (product.price * cart[k]['quantity'])
            order['get_cart_total'] += total
            order['get_cart_items'] += cart[k]['quantity']

            item = {
                'product':{
                    'id':product.id,
                    'name':product.name,
                    'price':product.price,
                    #'digital':product.digital,
                    'imageURL': product.imageURL
                },
                'quantity': cart[k]['quantity'],
                'get_total': total
            }

            items.append(item)

            if product.digital == False:
                order['shipping'] = True
        except:
            pass

    return {'items':items, 'order':order, 'cartItems':cartItems}