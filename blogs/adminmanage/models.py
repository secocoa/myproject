import os

from django.db import models

# Create your models here.
from django.utils import timezone


class MyManager(models.Manager):
    def get_queryset(self):
        return  super().get_queryset().filter(is_delete=False)

class User(models.Model):
    uname = models.CharField(unique=True,max_length=10)
    password = models.CharField(max_length=32)
    phone = models.CharField(max_length=11)
    is_delete = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    umanager = MyManager()
    class Meta:
        db_table = 'user'


class User_info(models.Model):
    user = models.OneToOneField(User)
    idcard = models.CharField(max_length=18)
    realname = models.CharField(max_length=10)
    email = models.EmailField(null=True)
    lastlogin = models.DateTimeField(default=timezone.now())
    headportrait=models.CharField(max_length=50,null=True)

    class Meta:
        db_table = 'user_info'
class Category(models.Model): # 文章栏目
    cname = models.CharField(max_length=15,unique=True)
    is_delete = models.BooleanField(default=False)
    cmanager = MyManager()

    class Meta:
        db_table = 'category'

class Label(models.Model): #文章标签
    lname = models.CharField(max_length=15)
    category = models.ForeignKey(Category)
    is_delete = models.BooleanField(default=False)

    lmanager  = MyManager()

    class Meta:
        db_table = 'label'

class Blog(models.Model):
    btitle = models.CharField(max_length=20,null=True)
    creat_time = models.DateTimeField(default=timezone.now)
    abstract = models.CharField(max_length=100,null=True)
    body = models.CharField(max_length=150)
    author = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    label = models.ManyToManyField(Label)
    is_savedraft = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    is_prvite = models.BooleanField(default=False)
    is_comment = models.BooleanField(default=False)
    files = models.CharField(null=True,max_length=150)


    bmymanager = MyManager()

    class Meta:
        db_table = 'blog'

class Visitnum(models.Model):
    user = models.ForeignKey(User)
    blog = models.ForeignKey(Blog)
    is_like = models.BooleanField(default=True)

    class Meta:
        db_table = 'visitnum'

class Comments(models.Model):  #评论
    body = models.TextField()
    user = models.ForeignKey(User)
    blog = models.ForeignKey(Blog)
    is_delete = models.BooleanField(default=False)

    commanager = MyManager()
    class Meta:
        db_table = 'comments'


