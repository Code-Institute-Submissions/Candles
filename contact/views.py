from django.shortcuts import render

def emailContact(request):
    
    if request.method == 'POST':
       message_name = request.POST['message-name']
       message_email = request.POST['message-email']
       message = request.POST['message']
       context = {'menu_class': 'menu-login', 'message_name': message_name}
       return render(request, 'contact/emailSent.html', context)
    else:
        context = {'menu_class': 'menu-login'}
        return render(request, 'contact/email.html', context)

def emailSentConfirm(request):
    context = {'menu_class': 'menu-login'}
    return render(request, 'contact/emailSent.html', context)
