from django.shortcuts import render

from products.models import *

def displayShop(request):
    products = Product.objects.all()
    return render(request, 'shop/store.html', {'products':products})
