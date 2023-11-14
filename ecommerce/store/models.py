from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    #           relación 1 a 1 con la tabla User
    #           un usuario solo tiene un cliente
    #           un cliente solo tiene un usuario             if user is deleted, delete this item
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        #return self.name
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    #if the product is digital, we do not need to send it
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    #lets avoid a problem if an item doesnot han an image
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Order(models.Model):
    #               un cliente puede tener muchas órdenes
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)# open car and we can keep adding more items
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return str(self.id)#cuz id is an integer
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
    @property
    def shipping(self):
        shipping = False
        orderItems = self.orderitem_set.all()
        for k in orderItems:
            if k.product.digital == False:
                shipping = True
        
        return shipping
    

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.product.name
    
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.address