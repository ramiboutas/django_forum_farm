from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

COUNTRY_CHOICES = (
    ('Nig','Nigeria'),
    ('AF', 'Afghanistan'),
    ('AL' ,'Albania'),
    ('DZ' , 'Algeria'),
    ('AX' , 'Aland'),
    ('AS' , 'American'),
    ('AI' , 'Anguilla'),
    ( 'AD' , 'Andorra'),
    ('AO' , 'Angola'),
    ('AN' ,' Antilles - Netherlands'),
)

class Farm(models.Model):
    farm_name = models.CharField(max_length=200, blank = True)
    recorded_by = models.ForeignKey(User, default= None, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.farm_name

class Address(models.Model):
    street_name = models.CharField(max_length = 200, blank = True)
    street_no = models.CharField(max_length = 50, blank = True)
    city = models.CharField(max_length = 200)
    state = models.CharField(max_length = 200)
    country = models.CharField(max_length = 200, choices=COUNTRY_CHOICES, default='Nig')
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)

    def __str__(self):
        return self.city + ' ' + self.state + ' ' + self.country

class Telephone(models.Model):
    phonenumber = models.CharField(max_length = 200)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)

    def __str__(self):
        return self.phonenumber
