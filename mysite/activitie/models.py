from django.db import models

class Activity(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Activities_images',blank=True,null=True)
    location = models.URLField(null=True,blank=True)
    duration = models.CharField(max_length=240,null =True,blank=True)
    description = models.CharField(max_length=510)
    price = models.FloatField()
    details = models.CharField(max_length=600)
    def __str__(self):
        return self.name
        
    