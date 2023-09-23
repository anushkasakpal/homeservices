from django.db import models

SERVICE_CHOICES = (
    ('electrician','ELECTRICIAN'),
    ('plumber', 'PLUMBER'),
    ('cleaner','CLEANER'),
    ('painter','PAINTER'),
    ('carpenter','CARPENTER'),
    ('welder','WELDER'),
)

class usermodel(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    services = models.CharField(max_length=50,choices=SERVICE_CHOICES)
    serviceTime = models.DateTimeField()
    serviceDate = models.DateField()
    state = models.CharField(max_length=20)
    pincode = models.IntegerField()