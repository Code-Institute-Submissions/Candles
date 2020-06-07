import stripe

from django.shortcuts import render
from products.models import *
from payment import *
from review.models import Review


def displayShop(request):
    products = Product.objects.all()
    context = {'products': products, 'menu_class': 'menu-shop'}
    return render(request, 'shop/store.html', context)

def displayProduct(request, pk):
    product = Product.objects.get(id=pk)
    reviews = Review.objects.filter(product_id=pk).order_by('-date').values()
    context = {'product':product, 'reviews': reviews}
    return render(request, 'shop/displayProduct.html', context)
