from django.db import models
from mongoengine import *

# Create your models here.

class Grade(models.Model):
    sID = models.CharField(max_length=10, null=True)
    term = models.IntegerField(null=True)
    year = models.IntegerField(null=True)
    grade = models.FloatField(null=True)
    gpa = models.FloatField(null=True)