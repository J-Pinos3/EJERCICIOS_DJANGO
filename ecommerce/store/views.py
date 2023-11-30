from django.shortcuts import render
from django.http import JsonResponse

import json
import datetime
from .models import *


def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False} 
        cartItems = order['get_cart_items']

    products = Product.objects.all()

    context = {'products':products, 'cartItems':cartItems}
    return render(request, 'store/store.html', context)


def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        #if can not find an item, create it
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        #items = OrderItem.objects.filter(order=order)
        cartItems = order.get_cart_items
        # all the order-items that have order as a parent
        items = order.orderitem_set.all()
    else:
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
            cartItems += cart[k]['quantity']
    return render(request, 'store/cart.html', {'items':items, 'order':order, 'cartItems':cartItems})


def checkout(request): 
    if request.user.is_authenticated:
        customer = request.user.customer
        #if can not find an item, create it
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        #items = OrderItem.objects.filter(order=order)
        cartItems = order.get_cart_items
        # all the order-items that have order as a parent
        items = order.orderitem_set.all()
    else:
        items=[]
        #if user is not authenticated the code above will throw an error
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']
    context = {'items':items, 'order':order,'cartItems':cartItems}
    return render(request, 'store/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id = productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem , created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    #print("Data: ", request.body)
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data["form"]["total"])#user data
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        
        order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order = order,
            address=data["shipping"]["address"],
            city=data["shipping"]["city"],
            state=data["shipping"]["state"],
            zipcode=data["shipping"]["zipcode"],
        )

    else:
        print("User is not logged in")

    return JsonResponse("Payment completed", safe=False)