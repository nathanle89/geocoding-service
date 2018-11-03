from rest_framework import status
from rest_framework.test import APISimpleTestCase

class AccountTests(APISimpleTestCase):

    def test_base_url(self):
        response = self.client.get('', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_missing_lat_long(self):
        response = self.client.get('/api/v1/location', format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], "Missing Latitude and Longitude")

    def test_missing_lat(self):
        response = self.client.get('/api/v1/location?longitude=1', format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], "Missing Latitude")

    def test_missing_long(self):
        response = self.client.get('/api/v1/location?latitude=1', format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], "Missing Longitude")

    def test_invalid_lat_long(self):
        response = self.client.get('/api/v1/location?latitude=bad&longitude=bad', format='json')
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(response.data['detail'], "Latitude and Longitude must be a number")

    def test_no_result_found(self):
        response = self.client.get('/api/v1/location?latitude=1&longitude=1', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "No result found")

    def test_valid_result(self):
        response = self.client.get('/api/v1/location?latitude=37.3756518&longitude=-122.0289512', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['city'], "Sunnyvale")
        self.assertEqual(response.data['country'], "USA")
        self.assertEqual(response.data['postal'], "94086")
