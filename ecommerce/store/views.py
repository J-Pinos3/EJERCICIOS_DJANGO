from django.shortcuts import render
from .models import *


def store(request):

    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/store.html', context)


def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        #if can not find an item, create it
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        #items = OrderItem.objects.filter(order=order)
        # all the order-items that have order as a parent
        items = order.orderitem_set.all()
    else:
        items=[]
        #if user is not authenticated the code above will throw an error
        order = {'get_cart_total':0, 'get_cart_items':0}
    return render(request, 'store/cart.html', {'items':items, 'order':order})


def checkout(request): 
    if request.user.is_authenticated:
        customer = request.user.customer
        #if can not find an item, create it
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        #items = OrderItem.objects.filter(order=order)
        # all the order-items that have order as a parent
        items = order.orderitem_set.all()
    else:
        items=[]
        #if user is not authenticated the code above will throw an error
        order = {'get_cart_total':0, 'get_cart_items':0} 
    context = {'items':items, 'order':order}
    return render(request, 'store/checkout.html', context)