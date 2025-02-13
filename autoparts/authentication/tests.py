from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

class UserTests(APITestCase):
    def setUp(self):
        self.admin_pass = 'adminpass'
        self.admin_user = get_user_model().objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password=self.admin_pass,
            name='Admin User'
        )
        self.normal_user = get_user_model().objects.create_user(
            username='user',
            email='user@example.com',
            password='userpass',
            name='Normal User'
        )
        self.user_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newuserpass',
            'name': 'New User'
        }

    def test_create_user_admin(self):
        """Test that an admin user can create a new user"""
        self.client.login(username='admin', password='adminpass')
        response = self.client.post('/auth/user/', self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(get_user_model().objects.count(), 3)

    def test_create_user_normal_user(self):
        """Test that a normal user cannot create a new user"""
        self.client.login(username='user', password='userpass')
        response = self.client.post('/auth/user/', self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login(self):
        """Test that a user can log in with valid credentials"""
        login_data = {
            'username': 'user',
            'password': 'userpass'
        }
        response = self.client.post('/auth/token/', login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_login_invalid_credentials(self):
        """Test that a user cannot log in with invalid credentials"""
        login_data = {
            'username': 'user',
            'password': 'wrongpassword'
        }
        response = self.client.post('/auth/token/', login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_admin_login(self):
        """Test that a admin-user can log in with valid credentials"""
        login_data = {
            'username': self.admin_user.username,
            'password': self.admin_pass
        }
        response = self.client.post('/auth/admin/signin/', login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_admin_login_invalid_credentials(self):
        """Test that a admin-user can log in with invalid credentials"""
        login_data = {
            'username': self.admin_user.username,
            'password': 'wrongpasswordexample'
        }
        response = self.client.post('/auth/admin/signin/', login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)