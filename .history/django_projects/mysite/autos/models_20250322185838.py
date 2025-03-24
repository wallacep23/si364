from django.db import models

# Create your models here.
class Make(models.Model):
    name = models.CharField(max_length=200)

class Auto(models.Model):
    nickname = models.CharField(max_length=200)
    mileage = models.IntergerField()
    comments = models.CharField(max_length=300)
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    