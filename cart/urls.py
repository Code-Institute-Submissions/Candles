from django.urls import path

from . import views

urlpatterns = [
    path('', views.display_cart, name='displayCart'),
    path('add/<str:id>/', views.add_item_to_cart, name='addToCart'),
    path('checkout/', views.checkout, name='displayCheckout'),
]