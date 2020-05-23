from django.urls import path

from . import views

urlpatterns = [
    path('', views.cart, name='displayCart'),
    path('checkout/', views.checkout, name='displayCheckout'),
]