from django.urls import path

from . import views

urlpatterns = [
    path('', views.emailContact, name='emailContact'),
    path('emailSent/', views.emailSentConfirm, name='emailSent'),
]