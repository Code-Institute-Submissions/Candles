from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=254, default='')
    last_name = models.CharField(max_length=254, default='')
    phone = models.CharField(max_length=254, default='')
    email = models.EmailField(max_length=254, default='')
    address_1 = models.CharField(max_length=254, default='')
    address_2 = models.CharField(max_length=254, default='')
    address_3 = models.CharField(max_length=254, default='')
    address_4 = models.CharField(max_length=254, default='')
    postcode = models.CharField(max_length=254, default='')
    #is_registered_user = models.BooleanField(default='False')

    def __str__(self):
        return self.name
