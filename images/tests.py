from django.test import TestCase
from .models import Gallery, GalleryImage, tags

# Create your tests here.
class GalleryTestClass(TestCase):
    def setUp(self):
        self.fun=Gallery(title = 'fun')

        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.fun,Gallery))

