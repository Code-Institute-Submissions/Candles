from django.shortcuts import render

# Create your views here.
def cart(request):
    return render(request, 'cart/cart.html')

def checkout(request):
    context = {'menu_class': 'menu-container'}
    return render(request, 'cart/checkout.html', context)
