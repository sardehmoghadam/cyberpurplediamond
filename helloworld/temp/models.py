from django.db import models

# Create your models here.

class contactmodel(models.Model):

    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    subject = models.CharField(max_length=64)
    desc = models.CharField(max_length=1024)

    def __str__(self):
        return f"{self.name} , {self.email} , {self.subject} "
class users(models.Model):

    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    key = models.CharField(max_length=1024)
    salt = models.CharField(max_length=1024)

    def __str__(self):
        return f"{self.name}"



