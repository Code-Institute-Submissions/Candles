from django.shortcuts import render, redirect, reverse
from products.models import Product


# Create your views here.
def display_cart(request):
    return render(request, 'cart/cart.html')

def checkout(request):
    context = {'menu_class': 'menu-container'}
    return render(request, 'cart/checkout.html', context)

def add_item_to_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)
    request.session['cart'] = cart
    return render(request, 'cart/cart.html')