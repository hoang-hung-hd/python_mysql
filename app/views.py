from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.utils.timezone import datetime
import re

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
    context= {'products': products}
    return render(request, 'app/home.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        if created:
            items = []
            print('you dont have any items in order')
        else:
            items = order.orderitem_set.all()
            print("have result " + str(items))
    else:
        items = []
    context= {'items': items, 'order': order}
    return render(request, 'app/cart.html', context)

def checkout(request):
    context= {}
    return render(request, 'app/checkout.html', context)
