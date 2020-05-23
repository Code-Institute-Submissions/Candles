from decimal import Decimal
from django.conf import settings
from products.models import Product

class Cart(object):

    def __init__(self, request):
        """
        Initialise the car
        """
        self.session = request.session
        cart =  self.session.get(settings.CART_ID)
        if not cart:
            cart = self.session[settings.CART_ID] = {}
        self.cart = cart

    