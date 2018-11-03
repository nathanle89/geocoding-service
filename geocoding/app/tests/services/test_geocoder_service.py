from django.test import SimpleTestCase
from app.services.geocoder_service import GeocoderService

class GeocoderServiceTestClass(SimpleTestCase):

    def setUp(self):
        pass

    def test_lookup_valid_result(self):
        result = GeocoderService.lookup(37.3756518, -122.0289512)

        self.assertEqual(result is not None, True)
        self.assertEqual(result['city'], 'Sunnyvale')
        self.assertEqual(result['country'], 'USA')
        self.assertEqual(result['postal'], '94086')

    def test_lookup_invalid_result(self):
        result = GeocoderService.lookup(1, 1)

        self.assertEqual(result, {})
