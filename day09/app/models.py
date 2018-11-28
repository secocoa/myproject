from django.db import models

# Create your models here.
class User(models.Model):
    uname = models.CharField(max_length=20)
    password = models.CharField(max_length=32)
    uage = models.IntegerField(default=20)