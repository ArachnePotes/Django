from django.db import models

class satff(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='staff_images',blank=True,null=True)
    role = models.CharField(max_length=255)

    def __str__(self):
        return self.name