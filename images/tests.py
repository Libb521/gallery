from django.test import TestCase
from .models import Image, tags

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.fun=Image(title = 'fun')

        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.fun,Image))

