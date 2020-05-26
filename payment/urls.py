from django.urls import path

from . import views

urlpatterns = [
    path('', views.paymentView, name='stripePayment'),
    path('success/', views.stripeSuccess, name='stripeSuccess'),
    path('cancel/', views.stripeCancel, name='stripeCancel'),
]