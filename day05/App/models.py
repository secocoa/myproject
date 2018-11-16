from django.db import models

# Create your models here.

#onetoone
class Student(models.Model):
    sname = models.CharField(max_length=30)

    def __str__(self):
        return  self.sname

    class Meta:
        db_table = 'student'


#档案
class Archive(models.Model):
    phone = models.CharField(max_length=11)
    # 一对一
    student = models.OneToOneField(Student,on_delete=models.PROTECT)

    def __str__(self):
        return self.phone

    class Meta:
        db_table = 'archive'


