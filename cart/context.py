from django.shortcuts import get_object_or_404
from products.models import Product

def cart_content(request):
    cart = request.session.get('cart', {})

    cart_items = []
    total_price = 0
    product_total = 0

    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total_price += quantity * product.price
        product_total += quantity
        cart_items.append({'id':id, 'quantity':quantity, 'product':product })

    return {'cart_items': cart_items, 'total_price': total_price, 'product_total': product_total}


    
