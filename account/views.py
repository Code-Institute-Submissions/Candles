from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm

def memberAreaDisplay(request):
    context = {'menu_class': 'menu-login'}
    return render(request, 'account/memberArea.html', context)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '\
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
        context = {'form': form, 'menu_class': menu-login}
    return render(request, 'account/login.html', context)

@login_required
def dashboard(request):
    context = {'section': 'dashboard', 'menu_class': 'menu-login'}
    return render(request,
                    'account/dashboard.html',
                    context)

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password1']
            )
            new_user.save()
            context = {'new_user':new_user}
            return render(request, 'account/register_done.html', context)
    else:
        user_form = UserRegistrationForm()
        context = {'user_form':user_form}
    return render(request, 'account/register.html', context)
