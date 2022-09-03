from django.db import models

class User (models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=8)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=200)
