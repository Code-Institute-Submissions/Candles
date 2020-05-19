from django.shortcuts import render
from .models import Cart

def display_cart(request):
    cart = Cart.objects.all()[0]
    context = {'cart':cart, 'menu_class':'menu-container'}
    return render(request, 'cart/display_cart.html', context)

