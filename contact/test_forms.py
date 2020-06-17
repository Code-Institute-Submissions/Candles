from django.test import TestCase

from .forms import SendEmailMessage

class SendEmailFormTest(TestCase):

    def test_send_email_form_name_field_label(self):
        form_data = {'message_name':'Tester',
        'message_email':'email@email.com', 'message_body':'This is the body of text to send'}
        form = SendEmailMessage(data=form_data)
        self.assertTrue(form.fields['message_name'].label_suffix == 'Your name')

    def test_send_email_form_email_field_label(self):
        form_data = {'message_name':'Tester',
        'message_email':'email@email.com', 'message_body':'This is the body of text to send'}
        form = SendEmailMessage(data=form_data)
        self.assertTrue(form.fields['message_email'].label_suffix == 'Your email')

    def test_send_email_form_body_field_label(self):
        form_data = {'message_name':'Tester',
        'message_email':'email@email.com', 'message_body':'This is the body of text to send'}
        form = SendEmailMessage(data=form_data)
        self.assertTrue(form.fields['message_body'].label_suffix == 'Your message here please')

    def test_send_email_form_is_valid_with_valid_data(self):
        form_data = {'message_name':'Tester',
        'message_email':'email@email.com', 'message_body':'This is the body of text to send'}
        form = SendEmailMessage(data=form_data)
        self.assertTrue(form.is_valid())

    def test_send_email_form_is_invalid_with_invalid_data(self):
        form_data = {'message_name':'Tester',
        'message_email':'email', 'message_body':'This is the body of text to send'}
        form = SendEmailMessage(data=form_data)
        self.assertFalse(form.is_valid())

