from django.test import TestCase
from django.core  import mail
from django.http import HttpResponse, HttpRequest
from .views import emailContact

class EmailTest(TestCase):
    def test_client_message_email_sent(self):
        mail.send_mail(
            'Subject of Message',
            'This is the message body',
            'from@email.com',
            ['to@email.com'],
            fail_silently=False,
        )

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Subject of Message')
        self.assertTemplateUsed('/contact/emailSent.html')

    

