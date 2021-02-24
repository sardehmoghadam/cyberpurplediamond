from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.models import PermissionsMixin


# Create your models here.

class contactmodel(models.Model):

    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    subject = models.CharField(max_length=64)
    desc = models.CharField(max_length=1024)
    readed = models.BooleanField()

    def __str__(self):
        return f"Email: {self.email} , Subject: {self.subject}, Readed: {self.readed} "

# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True, blank=False, null=False)

    # User._meta.get_field('email')._unique = True
    # User._meta.get_field('email').blank = False
    # User._meta.get_field('email').null = False

class blog(models.Model):

    topic = models.CharField(max_length=1024)
    content = models.TextField()
    reference = models.CharField(max_length=128)
    img = models.ImageField()
    month = models.IntegerField()
    year = models.IntegerField()
    totalread = models.IntegerField()

    def __str__(self):
        return f"{self.pk}: Topic: {self.topic} , Month: {self.month}, year: {self.year} "




