from django.db import models

# Create your models here.
class User(models.Model):
    uname = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    sex = models.BooleanField(default=True)
    age = models.IntegerField(default=0)
    def __str__(self):
        return self.uname

    class Meta:
        db_table = 'user'