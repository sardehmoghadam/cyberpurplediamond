from django.db import models

# Create your models here.
class Flight(models.Model):

    source = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.source} to {self.destination} with {self.price} price"
