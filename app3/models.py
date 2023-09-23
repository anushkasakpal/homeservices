from django.db import models

# Create your models here.
class adminmodel(models.Model):
    name = models.CharField(max_length=60)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=60)
    service = models.CharField(max_length=50)
    charges = models.IntegerField(default=2000)
