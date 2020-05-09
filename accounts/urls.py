from django.urls import path

from . import views

urlpatterns = [
    path('', views.membersArea, name='membersArea'),
    path('signupPage/', views.signupPage, name='signupPage'),
    path('login/', views.login_view, name='login'),
]