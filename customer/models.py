from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=254, default='')
    last_name = models.CharField(max_length=254, default='')
