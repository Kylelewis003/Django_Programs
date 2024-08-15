from django.db import models

# Create your models here.
class mymodel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    
