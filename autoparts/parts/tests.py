from decimal import Decimal
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from autoparts.parts.models import Part, CarParts
from autoparts.cars.models import Car

class PartViewSetTests(APITestCase):
    def setUp(self):
        self.admin_user = get_user_model().objects.create_superuser(
            username='admin', email='admin@example.com', password='adminpass'
        )
        self.normal_user = get_user_model().objects.create_user(
            username='user', email='user@example.com', password='userpass'
        )
        self.car = Car.objects.create(
            name='Corolla',
            manufacturer='Toyota',
            year=2020
        )
        self.part_data = {
            'part_number': '12345',
            'name': 'Brake Pad',
            'details': 'A quality brake pad',
            'price': 15.99,
            'quantity': 10
        }
        self.part = Part.objects.create(**self.part_data)
        self.car_part = CarParts.objects.create(car=self.car, part=self.part)

    def test_create_part_admin(self):
        """Test that an admin user can create a new part"""
        self.client.login(username='admin', password='adminpass')
        response = self.client.post('/parts/', self.part_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Part.objects.count(), 2)

    def test_create_part_normal_user(self):
        """Test that a normal user cannot create a new part"""
        self.client.login(username='user', password='userpass')
        response = self.client.post('/parts/', self.part_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_part(self):
        """Test that a user can retrieve a part"""
        self.client.login(username='user', password='userpass')
        response = self.client.get(f'/parts/{self.part.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_part_admin(self):
        """Test that an admin user can update a part"""
        self.client.login(username='admin', password='adminpass')

        update_data = {
            'part_number': '12345',
            'name': 'Updated Brake Pad',
            'details': 'Updated details for brake pad',
            'price': 79.99,
            'quantity': 50
        }
        
        response = self.client.put(f'/parts/{self.part.id}/', update_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.part.refresh_from_db()
        self.assertEqual(self.part.name, 'Updated Brake Pad')
        self.assertEqual(self.part.price, Decimal('79.99')) 
        self.assertEqual(self.part.quantity, 50)

    def test_update_part_normal_user(self):
        """Test that a normal user cannot update a part"""
        self.client.login(username='user', password='userpass')
        update_data = {'name': 'Updated Brake Pad'}
        response = self.client.put(f'/parts/{self.part.id}/', update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_part_admin(self):
        """Test that an admin user can delete a part"""
        self.client.login(username='admin', password='adminpass')
        response = self.client.delete(f'/parts/{self.part.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Part.objects.count(), 0)

    def test_delete_part_normal_user(self):
        """Test that a normal user cannot delete a part"""
        self.client.login(username='user', password='userpass')
        response = self.client.delete(f'/parts/{self.part.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_part_admin(self):
        """Test that an admin user can delete a part"""

        self.car_part.delete()

        self.client.login(username='admin', password='adminpass')

        response = self.client.delete(f'/parts/{self.part.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(Part.DoesNotExist):
            Part.objects.get(id=self.part.id)

    def test_create_car_part_normal_user(self):
        """Test that a normal user cannot create a new car part association"""
        self.client.login(username='user', password='userpass')
        car_part_data = {'car': self.car.id, 'part': self.part.id}
        response = self.client.post('/parts/carparts/', car_part_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_car_part_normal_user(self):
        """Test that a normal user cannot create a new car part association"""
        self.client.login(username='user', password='userpass')
        car_part_data = {'car': self.car.id, 'part': self.part.id}
        response = self.client.post('/parts/carparts/', car_part_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
