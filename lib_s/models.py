
from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    accredat = models.DateField()
    date = models.DateField()

    def __str__(self):
        return self.username  # This is optional, it's used for human-readable representation
    

class Log(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username  # This is optional, it's used for human-readable representation
