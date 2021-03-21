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

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id ,name, description , image_location, image_category):
        update = cls.objects.filter(id = id).update(name = name, description = description ,image_location = image_location,image_category = image_category)


class Location(models.Model):
    name = models.CharField(max_length =50)

class Category(models.Model):
    name = models.CharField(max_length =50)
