from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

from shop.views import *

def membersArea(request):
    return render(request, 'accounts/membersArea.html')

def signupPage(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('index'))
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signupPage.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(reverse('index'))
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})