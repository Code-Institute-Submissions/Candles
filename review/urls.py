from django.urls import path

from review import views

urlpatterns = [
    path('', views.writeReview, name='writeAReview'),
]