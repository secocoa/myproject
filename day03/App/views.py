from django.http import HttpResponse
from django.shortcuts import render
from hashlib import  md5 #内置库 md5用于签名
# Create your views here.
from App.models import User
from random import randint


def adduser(req):
    user = User()
    user.username = '王思聪' + str(randint(1,10000))
    user.password = md5(b'123').hexdigest()
    user.ip = '124.53.53.3'
    user.save()
    return  HttpResponse('添加新用户' + str(user.id))

def updateuser(req):
    # user = User.objects.first()
    # user.username = '隔壁老王'
    # user.save()
    # return  HttpResponse('修改用户成功')
    user = User.objects.all()
    user.update(ip='8.8.8.8')
    return  HttpResponse('修改用户成功')

def deleteuser(req):
    user = User.objects.last()
    user.delete()
    return  HttpResponse('删除用户成功')

def getqueryset(req):
    # users = User.objects.all()
    # res = users.filter(username='隔壁老王')
    # print(users)
    # print(type(users))
    # print(res)
    # print(type(users))
    # res = users.filter().filter(password='111',username='隔壁老王')

    # res = User.objects.exclude(username='王思聪')

    # res = User.objects.all().order_by('-id')
    # res = User.objects.all().order_by('-id','username')

    #res = User.objects.values('username','password')
    #print(res)


    # res = User.objects.all().values('username').distinct()

    res = User.objects.all().order_by('-id').reverse()
    print(res)

    # return render(req,'userlist.html',context={'data':res})
    return render(req, 'fields.html', context={'data': res})