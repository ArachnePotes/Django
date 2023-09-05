from django.db import models

# Create your models here.

class about(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='about_images',blank=True,null=True)
    descriptionESP = models.CharField(max_length=600)
    descriptionENG = models.CharField(max_length=600)
    ref = models.URLField(blank=True,null=True)
    def __str__(self):
        return self.name