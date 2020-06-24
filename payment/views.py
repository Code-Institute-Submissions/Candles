import stripe

from django.conf import settings
from django.shortcuts import render

stripe.api_key = settings.STRIPE_PUBLISHABLE_KEY

def paymentView(request):
    context = {'menu_class': 'menu-container'}
    return render(request, 'payment/paymentView.html', context)

def stripeSuccess(request):
    context = {'menu_class': 'menu-container'}
    return render(request, 'payment/success.html', context)

def stripeCancel(request):
    context = {'menu_class': 'menu-container'}
    return render(request, 'payment/canceled.html', context)

def charge(request):
   session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{'price': '{{PRICE_ID}}','quantity': 1,}],
        mode='payment',
        success_url='https://peggy535.pythonanywhere.com/payment/success/?session_id={CHECKOUT_SESSION_ID}',
        cancel_url='https://peggy535.pythonanywhere.com/payment/canceled/',
    )
