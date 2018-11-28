from django.db import models

# Create your models here.

class Student(models.Model):
    sname = models.CharField(max_length=20)
    ssex  = models.BooleanField(default=True)
    sage = models.IntegerField(null=True)

    def __str__(self):
        return self.sname
    class Meta:
        db_table = 'student'