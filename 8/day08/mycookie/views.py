from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse

from app.models import User


def index(request):
    uname = request.COOKIES.get('ll')
    return render(request,'mycookie/index.html',context={"uname":uname})


def login(request):
    if request.method=='GET':
        return render(request,'mycookie/login.html')
    else:
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        user = User.objects.filter(uname=uname,password=password)
        if user.exists():
            res = redirect(reverse('mycookies:index'))
            res.set_cookie('ll',uname)
            return  res
        else:
            return render(request,'mycookie/notice.html',context={
                'code': -1,
                'msg': '用户名或密码错误',
                'wait': 3,
                'url': reverse('mycookies:index'),
            })

def register(request):
    if request.method == 'GET':
        return render(request,'mycookie/regjster.html')
    else:
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        user = User()
        user.uname = uname
        user.password = password
        try:
            user.save()
        except Exception as e:
            print(e)
            return redirect(reverse('mycookies:register'))
        # session
        request.session['uname'] = uname
        request.session['password'] = password
        return  redirect(reverse('mycookies:register'))

def logout1(request):
    res = redirect(reverse("mycookies:index"))
    #删除cookie
    res.delete_cookie('ll')
    return res