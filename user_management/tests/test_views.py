from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from user_management.forms import RegistrationForm
from user_management.models import Crypto


class RegistrationViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.registration_url = reverse(
            'register')  # Replace 'register' with your actual URL name

    def test_get_request(self):
        response = self.client.get(self.registration_url)
        # Check that the response status code is 200
        self.assertEqual(response.status_code, 200)
        # Check that the correct template is used
        self.assertTemplateUsed(response, 'register.html')
        # Check that the form is an instance of RegistrationForm
        self.assertIsInstance(response.context['form'], RegistrationForm)

    def test_valid_post_request(self):
        data = {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'email': 'test@email.com'
        }

        response = self.client.post(self.registration_url, data)
        # Check that the response is a redirect (status code 302)
        self.assertEqual(response.status_code, 302)
        # Check that it redirects to the 'home' URL
        self.assertRedirects(response, reverse('home'))
        # Check that a new user was created
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_invalid_post_request(self):
        data = {
            'username': 'testuser',
            'password1': 'testpassword1',
            'password2': 'testpassword2',
            'email': 'test@email.com'
        }

        response = self.client.post(self.registration_url, data)
        # Check that the response is a redirect (status code 302)
        self.assertEqual(response.status_code, 302)
        # Check that it redirects back to the 'register' URL
        self.assertRedirects(response, reverse('register'))
        # Check that no new user was created due to the invalid form
        self.assertFalse(User.objects.filter(username='testuser').exists())


class LoginViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.user = User.objects.create_user(username='testuser',
                                             password='testpassword',
                                             email='test@email.com')

    def test_post_valid_credentials(self):
        response = self.client.post(self.login_url,
                                    {'username': 'testuser',
                                     'password': 'testpassword'})
        # Check for a redirect
        self.assertEqual(response.status_code, 302)
        # Verify redirection to the 'home' URL
        self.assertRedirects(response, reverse('home'))
        # Verify user is authenticated
        self.assertEqual(response.wsgi_request.user, self.user)

    def test_post_invalid_credentials(self):
        response = self.client.post(self.login_url,
                                    {'username': 'testuser',
                                     'password': 'invalidpassword'})
        # Check for rendering of login page
        self.assertEqual(response.status_code, 200)
        # Verify template used
        self.assertTemplateUsed(response, 'login.html')
        # Check for error message
        self.assertContains(response, "Invalid username or password.")
        # Verify user is not authenticated
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_get_request(self):
        response = self.client.get(self.login_url)
        # Check for rendering of login page
        self.assertEqual(response.status_code, 200)
        # Verify template used
        self.assertTemplateUsed(response, 'login.html')

    def test_empty_credentials(self):
        response = self.client.post(self.login_url,
                                    {'username': '', 'password': ''})
        # Check for rendering of login page
        self.assertEqual(response.status_code, 200)
        # Verify template used
        self.assertTemplateUsed(response, 'login.html')
        # Check for form validation errors
        self.assertContains(response, "Invalid username or password.")
        # Verify user is not authenticated
        self.assertFalse(response.wsgi_request.user.is_authenticated)


class LogoutViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.logout_url = reverse('logout')
        self.user = User.objects.create_user(username='testuser',
                                             password='testpassword')
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

    def test_logout(self):
        response = self.client.get(self.logout_url)
        # Check for a redirect
        self.assertEqual(response.status_code, 302)
        # Verify redirection to the 'home' URL
        self.assertRedirects(response, reverse('home'))
        # Verify user is not authenticated
        self.assertFalse(response.wsgi_request.user.is_authenticated)


class HomeViewTestCase(TestCase):
    def test_home_view(self):
        # Make a GET request to the home view
        response = self.client.get(reverse('home'))
        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Verify that the correct template is used
        self.assertTemplateUsed(response, 'home.html')
        # Check that the context data includes
        # 'articles' and 'cryptos_trending'
        self.assertIn('articles', response.context)
        self.assertIn('cryptos_trending', response.context)
        # Verify that the data in the context matches the mock data
        articles = response.context['articles']
        cryptos_trending = response.context['cryptos_trending']
        self.assertIsNotNone(articles)
        self.assertIsNotNone(cryptos_trending)


class ManageViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.manage_url = reverse('manage')

    def test_post_valid_data(self):
        data = {'crypto': 'bitcoin'}
        initial_crypto_count = Crypto.objects.count()
        response = self.client.post(self.manage_url, data)
        # Check for a redirect
        self.assertEqual(response.status_code, 302)
        # Verify redirection to the 'manage' URL
        self.assertRedirects(response, reverse('manage'))
        # Check that a new Crypto object was created
        self.assertEqual(Crypto.objects.count(), initial_crypto_count + 1)

    def test_post_invalid_data(self):
        data = {'crypto': ''}
        initial_crypto_count = Crypto.objects.count()
        response = self.client.post(self.manage_url, data)
        # Check for a redirect
        self.assertEqual(response.status_code, 302)
        # Verify redirection to the 'manage' URL
        self.assertRedirects(response, reverse('manage'))
        # Check that no new Crypto object was created
        self.assertEqual(Crypto.objects.count(),
                         initial_crypto_count)

    def test_get_request(self):
        response = self.client.get(self.manage_url)
        # Check for rendering of 'manage.html'
        self.assertEqual(response.status_code, 200)
        # Verify template used
        self.assertTemplateUsed(response, 'manage.html')
        # Check that 'cryptos' is in the context data
        self.assertIn('cryptos', response.context)
        # Check that 'add_crypto_form' is in the context data
        self.assertIn('add_crypto_form', response.context)


class DeleteCryptoViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.manage_url = reverse('manage')

    def test_post_delete_crypto(self):
        response = self.client.post(self.manage_url,
                                    {'crypto_name': 'bitcoin'})
        # Check for a redirect
        self.assertEqual(response.status_code, 302)
        # Verify redirection to the 'manage' URL
        self.assertRedirects(response, reverse('manage'))
