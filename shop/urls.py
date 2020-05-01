from django.urls import path

from . import views

urlpatterns = [
    path('', views.displayProducts, name='displayProducts'),
]