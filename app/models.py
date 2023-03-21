from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    userID = models.OneToOneField(User, on_delete = models.SET_NULL, null=True, blank=False)
    userName = models.CharField(max_length=200, null=True)
    userEmail = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.userName
    
class Product(models.Model):
    productName = models.CharField(max_length=200, null=True)
    productPrice = models.FloatField()
    productImage = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.productName
    
    @property
    def ImageURL(self):
        try:
            url = self.productImage.url
        except:
            url = ''
        return url
    
class Order(models.Model):
    customer = models.ForeignKey( Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_order = models.DateTimeField( auto_now_add=True)
    isComplete = models.BooleanField( default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.transaction_id
    
class Order_Item(models.Model):
    Product = models.ForeignKey( Product, on_delete=models.SET_NULL, blank=True, null=True)
    Order = models.ForeignKey( Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)    

class ShippingAddress(models.Model):
    customer = models.ForeignKey( Customer, on_delete=models.SET_NULL, blank=True, null=True)
    Order = models.ForeignKey( Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    mobile = models.CharField(max_length=20, null=True)
    date_added = models.DateTimeField(auto_now_add=True)    
    def __str__(self):
        return self.address
