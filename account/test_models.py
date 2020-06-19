from django.test import TestCase
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from .models import *


class ProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user_new = User.objects.create_user(username='newuser1', password ='1Xuyty89iu8')
        user_new.save()

    def test_field_name_of_username_correct(self):
        user = User.objects.get(username='newuser1')
        user.login(username='newuser1', password ='1Xuyty89iu8')
        field_label = user._meta.get_field('username').verbose_name
        self.assertEquals(field_label, 'username')
    
    
    