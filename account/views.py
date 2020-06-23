from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm, EditUserForm, EditProfileForm
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile

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
        context = {'form': form, 'menu_class': 'menu-login'}
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
            Profile.objects.create(user=new_user)
            context = {'new_user':new_user, 'menu_class': 'menu-login'}

            message_name = user_form.cleaned_data['first_name']
            message_email = user_form.cleaned_data['email']
            message = EmailMessage(
                subject="Welcome "+str(message_name)+" to 0&X Candles",
                to=[str(message_email)],
                )
            message.template_id = 2  # use this Sendinblue template
            message.from_email = None  # to use the template's default sender
            message.merge_global_data = {'name': message_name,}
            message.send()

            return render(request, 'account/register_done.html', context)
    else:
        user_form = UserRegistrationForm()
        context = {'user_form':user_form, 'menu_class': 'menu-login'}
    return render(request, 'account/register.html', context)

@login_required
def editProfile(request):
    if request.method == 'POST':
        user_form = EditUserForm(instance=request.user, data=request.POST)
        profile_form = EditProfileForm(instance=request.user.profile, data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            context = {'menu_class': 'menu-login'}
        return render(request, 'account/profileUpdated.html', context)
    else:
        user_form = EditUserForm(instance=request.user)
        profile_form = EditProfileForm(instance=request.user.profile)

    context = {'user_form':user_form, 'profile_form': profile_form, 'menu_class': 'menu-login'}
    return render(request, 'account/editProfile.html', context)


