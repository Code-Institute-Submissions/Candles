from django.db import models
from django.conf import settings

"""
Creating a user member profile model. This has a one-to-one relationship with 
the new user created from UserRegistrationForm in the Member Area of the site.
Specific and more relevant/detailed personal information will be stored in this
model.
"""
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    address1 = models.CharField(max_length=254, default='')
    address2 = models.CharField(max_length=254, default='')
    address3 = models.CharField(max_length=254, default='', blank=True)
    address4 = models.CharField(max_length=254, default='', blank=True)
    postcode = models.CharField(max_length=50, default='')

    def __str__(self):
        return f'Profile for user {self.user.username}'