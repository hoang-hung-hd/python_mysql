from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from django.utils.timezone import datetime
import re
import json

# Create your views here.

def hello_there(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return HttpResponse(content)

def get_home(request):
    products = Product.objects.all()
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
        if created:
            items = []
            print('you dont have any items in order')
        else:
            items = order.orderitem_set.all()          
    else:
        items = []
        order = { 'get_cart_items': 0, 'get_cart_total': 0}
        cartItems = order['get_cart_items']

    context= {'products': products, 'cartItems': cartItems}
    return render(request, 'app/home.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
        if created:
            items = []
            print('you dont have any items in order')
        else:
            items = order.orderitem_set.all()          
    else:
        items = []
        order = { 'get_cart_items': 0, 'get_cart_total': 0}
        cartItems = order['get_cart_items']
    context= {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'app/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
        if created:
            items = []
            print('you dont have any items in order')
        else:
            items = order.orderitem_set.all()          
    else:
        items = []
        order = { 'get_cart_items': 0, 'get_cart_total': 0}
        cartItems = order['get_cart_items']
    context= {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'app/checkout.html', context)

def updateItems(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user.customer
    product = Product.objects.get(id = productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderitem, created = OrderItem.objects.get_or_create( order=order, product = product)
    if action == 'add':
        orderitem.quantity +=1
    elif action == 'remove':
        orderitem.quantity = 0
    elif action == 'minus':
        orderitem.quantity -=1
    orderitem.save()

    if orderitem.quantity <= 0:
        orderitem.delete()

    return JsonResponse(action, safe = False)
