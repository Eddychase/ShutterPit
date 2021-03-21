from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length = 60)
    pic = models.ImageField(upload_to = 'uploads/')
    picture = ImageField( blank = True, manual_crop = '1920x1080')
    description = models.TextField()
    image_location = models.ForeignKey('Location')
    image_category = models.ForeignKey('Category')

class Location(models.Model):
    name = models.CharField(max_length =50)

class Category(models.Model):
    name = models.CharField(max_length =50)
