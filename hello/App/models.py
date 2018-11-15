from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    userpasswd = models.CharField(max_length=32)
class Goods(models.Model):
    goodname = models.CharField(max_length=20)
    userid = models.OneToOneField(User)
