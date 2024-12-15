from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.
class RegistrationPageTests(TestCase):
    def test_register_page_contains_required_fields(self):
        response = self.client.get(reverse('universe:register_or_login'))

        self.assertContains(response, '<input type="text" id="id_username" name="username" required>')
        self.assertContains(response, '<input type="password" id="id_password" name="password" required>')
        self.assertContains(response, '<input type="text" id="id_favorite_ttrpg" name="favorite_ttrpg">')
    
    def test_register_and_login(self):
        response = self.client.post(reverse('universe:register_or_login'), {
            'username': 'new_user',
            'password': 'securepassword123',
            'favorite_ttrpg': 'Dungeons and Dragons'
        })

        self.assertRedirects(response, reverse('main_home:home'))

        user = get_user_model().objects.get(username='new_user')
        self.assertTrue(user.is_authenticated)

class LoginTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='securepassword123')

    def test_login_redirects_to_home(self):
        response = self.client.post(reverse('universe:register_or_login'), {
            'username': 'testuser',
            'password': 'securepassword123',
            'login': '1'
        })

        self.assertRedirects(response, reverse('main_home:home'))

        user = get_user_model().objects.get(username='testuser')
        self.assertTrue(user.is_authenticated)

    def test_incorrect_credentials_show_error(self):
        response = self.client.post(reverse('universe:register_or_login'), {
            'username': 'testuser',
            'password': 'wrongpassword',  # Incorrect password
            'login': '1'
        })

        self.assertContains(response, "Invalid username or password.")

        user = get_user_model().objects.get(username='testuser')
        self.assertTrue(user.is_authenticated)

class LogoutTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='securepassword123')
        self.client.login(username='testuser', password='securepassword123')  # Log in user

    def test_user_logout(self):
        # Click "Log Out" and log out
        response = self.client.get(reverse('universe:logout'))  # Assuming the logout URL

        # Check that the user is logged out
        self.assertNotIn('_auth_user_id', self.client.cookies)  # Session should be cleared
        self.assertRedirects(response, reverse('main_home:home'))

    def test_redirect_after_logout(self):
        # Log out
        response = self.client.get(reverse('universe:logout'))

        # Check redirection to home page after logout
        self.assertRedirects(response, reverse('main_home:home'))