from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='service_images',blank=True,null=True)
    location = models.URLField(null=True)
    duration = models.CharField(max_length=240)
    description = models.CharField(max_length=510)
    price = models.FloatField()

    def __str__(self):
        return self.name
        
    