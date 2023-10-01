from django.test import TestCase
from user_management.forms import RegistrationForm, AddCryptoForm


class RegistrationFormTestCase(TestCase):
    def test_registration_form_valid(self):
        # Create a dictionary of valid form data
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        form = RegistrationForm(data=form_data)

        # Check if the form is valid
        self.assertTrue(form.is_valid())

    def test_registration_form_invalid(self):
        # Create a dictionary of invalid form data
        form_data = {
            'username': '',
            'email': 'invalid-email',
            'password1': 'password1',
            'password2': 'password2',
        }
        form = RegistrationForm(data=form_data)

        # Check if the form is invalid
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)


class AddCryptoFormTestCase(TestCase):
    def test_add_crypto_form_valid(self):
        # Create a dictionary of valid form data
        form_data = {
            'crypto': 'bitcoin',
        }
        form = AddCryptoForm(data=form_data)

        # Check if the form is valid
        self.assertTrue(form.is_valid())

    def test_add_crypto_form_invalid(self):
        # Create a dictionary of invalid form data
        form_data = {
            'crypto': 'nonexistent_crypto',
        }
        form = AddCryptoForm(data=form_data)

        # Check if the form is invalid
        self.assertFalse(form.is_valid())
        self.assertIn('crypto', form.errors)
