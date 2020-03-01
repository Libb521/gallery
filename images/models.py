from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

# Create your models here.
class Gallery(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=600)
    thumb = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(500)], format='JPEG', options={'quality': 90})
    tags = models.CharField(max_length=300)
    createad = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=60, unique=True)

    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ['title']

