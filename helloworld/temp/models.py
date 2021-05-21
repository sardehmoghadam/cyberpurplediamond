from django.db import models
from pyattck import Attck
from django.utils import timezone

attack = Attck()
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

class tactic(models.Model):

    identifier = models.CharField(max_length=64)
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.pk}: {self.identifier}"



class mitigation(models.Model):

    identifier = models.CharField(max_length=64)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=2048)
    stix = models.CharField(max_length=512)
    reference = models.CharField(max_length=2048)

    def __str__(self):
        return f"{self.pk}: {self.identifier}"


class technique(models.Model):

    rel_tactic = models.ForeignKey(tactic, on_delete=models.CASCADE)
    rel_mitigation = models.ManyToManyField(mitigation)
    identifier = models.CharField(max_length=64)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=2048)
    platform = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.pk}: {self.identifier}"

class subtechnique(models.Model):

    rel_technique = models.ForeignKey(technique, on_delete=models.CASCADE)
    identifier = models.CharField(max_length=64)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=2048)
    platform = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.pk}: {self.identifier}"

class maxview(models.Model):

    postid = models.IntegerField()
    postview = models.IntegerField()

    def __str__(self):
        return f"postID: {self.postid}, postview: {self.postview}"

class refer(models.Model):

    referid = models.IntegerField()

    def __str__(self):
        return f"referID: {self.referid}"