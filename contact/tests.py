from django.test import TestCase
from .forms import ContactForm
from django.urls import reverse


class ContactFormTest(TestCase):
    def test_valid_contact_form(self):
        form_data = {
            'name': 'Test User',
            'email': 'testuser@example.com',
            'message': 'This is a test message.',
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())
        contact = form.save()
        self.assertEqual(contact.name, 'Test User')
        self.assertEqual(contact.email, 'testuser@example.com')
        self.assertEqual(contact.message, 'This is a test message.')

    def test_invalid_contact_form(self):
        form_data = {
            'name': '',
            'email': 'invalid-email',
            'message': '',
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_contact_view(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
        self.assertIsInstance(response.context['form'], ContactForm)
