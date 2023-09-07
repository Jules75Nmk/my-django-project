from django.db import models

# Create your models here.
class Special(models.Model):
    appName= models.CharField(max_length=255)
    description= models.CharField(max_length=500)
    
