from django.db import models
from datetime import datetime
from django.utils.timezone import datetime

class Person(models.Model):
    registration_package = (
        ('Old Member','Old Member',),
        ('New Member','New Member'),
    )
    registration_type = models.CharField(max_length=20, choices=registration_package)
    Official_membership_no = models.IntegerField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender_option = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=gender_option)
    email = models.EmailField()
    password = models.CharField(max_length=16)
    password2 = models.CharField(max_length=16)
    phone_no = models.IntegerField()
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=15)
    lga = models.CharField(max_length=15)
