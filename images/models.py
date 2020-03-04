from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
import datetime as dt

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='image/', null=True)
    title = models.CharField(max_length=60)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=600)
    tags = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=60, unique=True)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ['title']

    @classmethod
    def search_by_title(cls,search_term):
        image = cls.objects.filter(title__icontains=search_term)
        return image
    
    @classmethod
    def days_image(cls, date):
        image = cls.objects.filter(pub_date__date=date)
        return image

    @classmethod
    def all_images(cls):
        image = cls.objects.all()
        return image

    def __str__(self):
        return self.name

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

