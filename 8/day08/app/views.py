import hashlib
import json
from _codecs import encode
from random import randint

from django.http import HttpResponse
from django.shortcuts import render, redirect
from hashlib import md5
# Create your views here.
from django.urls import reverse

from app.models import User
from app.sms import SMS


def adduser(request):
    user = User()
    user.uname = '佳佳%d' % randint(1,1000)
    user.password = md5(b'123').hexdigest()
    user.sex = randint(0,1)
    user.age = randint(15,25)
    user.save()
    return HttpResponse("增加用户%d" % user.id)


def homework(request):
    # res = json.dumps({'code':1,'msg':1})
    # res = request.GET.get('uname')
    res = json.dumps({'code':1,'msg':'用户已存在'})

    return HttpResponse(res)


def checkusername(request):
    return None


def register(request):
    return render(request,'register.html')


def login(request):
    if request.method == 'GET':
        return render(request,'mycookie/login.html')
    else:
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        password = hashlib.md5(password,encode('utf8'))
        user = User.objects.filter(uname=uname,password=password)
        if user.exists():
            res = redirect(reverse('app:index'))
            res.set_cookie('ll',uname)
            return res
        else:
            # render(request,'notice.html',context={
            #     'code': 1,
            #
            #     'msg':'用户名或密码错误，请重新填写',
            #     'wait':3,
            #     'url': reverse("app:login")
            # })
            return render(request,'mycookie/login.html')



def index(request):
    return None


def send(request):
   phonenumber =  request.GET.get('phone')
   sms = SMS("buildup","SMS_151578255")
   num = randint(100000,999999)
   res = sms.send_sms(phonenumber,num)
   return HttpResponse(res)


def dologin(request):
    return render(request,'app/login.html')