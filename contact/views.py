from django.conf import settings
from django.shortcuts import render
from django.core.mail import EmailMessage

from .forms import SendEmailMessage

def emailContact(request):
    if request.method == 'POST':
        form = SendEmailMessage(request.POST)
        if form.is_valid():
            message_name = form.cleaned_data['message_name']
            to_email = form.cleaned_data['message_email']
            message_body = form.cleaned_data['message_body']
            context = {'menu_class': 'menu-login', 'message_name': message_name}
            """
            These emails are sent to the client who has filled in the online email
            contact form on the Abount&Contact Page. A sendinblue template email
            is sent letting the client know their email has been received and 
            offers them information about a new product being launched. 'message2'
            is an email that is sent to the companies email address with the 
            clients message included and contact details.
            """
            message = EmailMessage(
                subject=str(message_name),
                body=str(message_body),
                to=[str(to_email)],
                )
            message.template_id = 1  # use this Sendinblue template
            message.from_email = None  # to use the template's default sender
            message.merge_global_data = {'name': message_name,}
            message.send()

            message2 = EmailMessage(
                subject="Message sent from website by "+str(message_name),
                body = str(message_body),
                from_email=str(to_email),
                to=['oandxcandles@gmail.com'],
            )
            message2.send()
            return render(request, 'contact/emailSent.html', context)
    else:
        form = SendEmailMessage()
        context = {'menu_class': 'menu-login', 'form': form}
        return render(request, 'contact/email.html', context)

def emailSentConfirm(request):
    context = {}
    return render(request, 'contact/emailSent.html', context)
