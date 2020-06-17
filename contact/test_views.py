from django.test import TestCase
from django.urls import reverse


class ContactViewTest(TestCase):
    def test_correct_contact_form_page_displayed_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_contact_view_url_accesible_by_name(self):
        response = self.client.get(reverse('emailContact'))
        self.assertEqual(response.status_code, 200)

    def test_correct_contact_email_view_template_used(self):
        response = self.client.get(reverse('emailContact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/email.html')

    
        

