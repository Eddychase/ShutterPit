from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.
class ImageTestClass(TestCase):
    def test_save_method(self):
        self.image.save_image()
        images  = Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_get_all_images(self):
        images = Image.get_all_images()
        self.assertTrue(len(images)>0)

    def test_get_image_by_id(self):
        images= Image.get_image_by_id(self.image.id)
        self.assertTrue(len(images) == 1)

    def test_search_by_category(self):
        images = Image.search_by_category('fashion')
        self.assertTrue(len(images)>0)

    def test_filter_by_location(self):
        images = Image.fil0ter_by_location('1')
        print(images)
        self.assertTrue(len(images)>0)
