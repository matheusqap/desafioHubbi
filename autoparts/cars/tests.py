from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from autoparts.cars.models import Car

class CarViewSetTests(APITestCase):
    def setUp(self):
        # Criação de um usuário admin com e-mail único
        self.admin_user = get_user_model().objects.create_superuser(
            username='admin', email='admin@example.com', password='adminpass'
        )
        # Criação de um usuário comum com e-mail único
        self.normal_user = get_user_model().objects.create_user(
            username='user', email='user@example.com', password='userpass'
        )

        # Criação de um carro para usar nos testes
        self.car_data = {
            'name': 'Corolla',
            'manufacturer': 'Toyota',
            'year': 2020
        }
        self.car = Car.objects.create(**self.car_data)

    def test_create_car_admin(self):
        """Test that an admin user can create a new car"""
        self.client.login(username='admin', password='adminpass')
        response = self.client.post('/cars/', self.car_data, format='json')
        self.assertEqual(response.status_code, 201)  # Status 201 CREATED
        self.assertEqual(Car.objects.count(), 2)  # Verifica se um novo carro foi criado

    def test_create_car_normal_user(self):
        """Test that a normal user cannot create a new car"""
        self.client.login(username='user', password='userpass')
        response = self.client.post('/cars/', self.car_data, format='json')
        self.assertEqual(response.status_code, 403)  # Espera um Forbidden

    def test_retrieve_car(self):
        """Test that a user can retrieve a car"""
        self.client.login(username='user', password='userpass')
        response = self.client.get(f'/cars/{self.car.id}/')
        self.assertEqual(response.status_code, 200)  # Status 200 OK

    def test_update_car_admin(self):
        """Test that an admin user can update a car"""
        self.client.login(username='admin', password='adminpass')

        update_data = {
            'name': 'Updated Corolla',
            'manufacturer': 'Toyota',
            'year': 2021
        }
        
        response = self.client.put(f'/cars/{self.car.id}/', update_data, format='json')

        self.assertEqual(response.status_code, 200)  # Status 200 OK
        self.car.refresh_from_db()
        self.assertEqual(self.car.name, 'Updated Corolla')
        self.assertEqual(self.car.year, 2021)

    def test_update_car_normal_user(self):
        """Test that a normal user cannot update a car"""
        self.client.login(username='user', password='userpass')
        update_data = {'name': 'Updated Corolla'}
        response = self.client.put(f'/cars/{self.car.id}/', update_data, format='json')
        self.assertEqual(response.status_code, 403)  # Espera um Forbidden

    def test_delete_car_admin(self):
        """Test that an admin user can delete a car"""
        self.client.login(username='admin', password='adminpass')
        response = self.client.delete(f'/cars/{self.car.id}/')
        self.assertEqual(response.status_code, 204)  # Status 204 NO CONTENT
        self.assertEqual(Car.objects.count(), 0)  # Verifica que o carro foi deletado

    def test_delete_car_normal_user(self):
        """Test that a normal user cannot delete a car"""
        self.client.login(username='user', password='userpass')
        response = self.client.delete(f'/cars/{self.car.id}/')
        self.assertEqual(response.status_code, 403)  # Espera um Forbidden
