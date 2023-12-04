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


def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        #if can not find an item, create it
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        #items = OrderItem.objects.filter(order=order)
        cartItems = order.get_cart_items
        # all the order-items that have order as a parent
        items = order.orderitem_set.all()

    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']

    return {'items':items, 'order':order,'cartItems':cartItems}


def guestOrder(request, data):
    print("User is not logged in")
    print("Cookies: ", request.COOKIES)
    name = data['form']['name']
    email = data['form']['email']
    
    cookieData = cookieCart(request)
    items = cookieData['items']

    customer, created = Customer.objects.get_or_create(
        email = email,
    )

    customer.name = name
    customer.save()

    order = Order.objects.create(
        customer = customer,
        complete=False
    )

    for item in items:
        product = Product.objects.get(id=item['product']['id'])

        orderItem = OrderItem.objects.create(
            product = product,
            order = order,
            quantity = item['quantity']
        )
    return customer, order