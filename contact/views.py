from django.shortcuts import render

def emailContact(request):
    context = {'menu_class': 'menu-login'}
    return render(request, 'contact/email.html', context)
