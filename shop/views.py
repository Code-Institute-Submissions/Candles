from django.shortcuts import render

def displayProducts(request):
    return render(request, 'shop/store.html')
