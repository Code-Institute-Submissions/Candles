from django.shortcuts import render
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from .models import *
from .forms import CreateUserRegForm

def registerPage(request):
    form = CreateUserRegForm()

    if request.method == 'POST':
        form = CreateUserRegForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'account/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'account/login.html', context)
