from django.urls import path

from . import views

urlpatterns = [
    path('', views.displayShop, name='displayShop'),
    path('<int:pk>/', views.displayProduct, name='displayProduct'),
]