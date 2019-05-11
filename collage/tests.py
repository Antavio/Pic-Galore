from django.test import TestCase
from .models import Location,Category,Image

class LocationTestClass(TestCase):
    def setUp(self):
        self.mombasa = Location(location='Mombasa')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.mombasa,Location))
    def test_save_method(self):
        self.mombasa.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

class CategoryTestClass(TestCase):
    def setUp(self):
        self.pets = Category(category='Animals')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.pets,Category))

    def test_save_method(self):
        self.pets.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)