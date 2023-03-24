from django.contrib import admin
from django.urls import path
from .  import views

urlpatterns = [
    path('', views.get_home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path('update_item/', views.updateItems, name="update_item"),
]