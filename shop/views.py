from django.shortcuts import render

from products.models import *

def displayShop(request):
    products = Product.objects.all()
    context = {'products': products, 'menu_class': 'menu-shop'}
    return render(request, 'shop/store.html', context)

def displayProduct(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product':product}
    return render(request, 'shop/displayProduct.html', context)