from django import forms

class SendEmailMessage(forms.Form):
    message_name = forms.CharField(max_length=50, label_suffix='Your name', required=True, widget=forms.TextInput) 
    message_email = forms.EmailField(max_length=50, label_suffix='Your email')
    message_body = forms.CharField(max_length=1000, required=True, label_suffix='Your message here please', help_text='1000 characters maximum.', widget=forms.Textarea(attrs={'rows':6, 'columns':5}))