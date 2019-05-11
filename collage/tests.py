from django.test import TestCase
from .models import Location,Category,Image

class LocationTestClass(TestCase):
    def setUp(self):
        self.mombasa = Location(location='Mombasa')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.mombasa,Location))
