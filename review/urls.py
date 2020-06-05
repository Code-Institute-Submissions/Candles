from django.urls import path

from . import views

urlpatterns = [
    path('', views.writeReview, name='writeAReview'),
]