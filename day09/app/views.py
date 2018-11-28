import hashlib
import os
from datetime import datetime
from random import randint

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.VerifyCode import VerifyCode
from app.models import User
from day09 import settings


def index(request):
    return HttpResponse("index")


def upload(request):
    return render(request,'app/fileupload.html')

def doupload(request):
    file =request.FILES['picture'] #获取文件对象
    print(type(file))
    print(file.name,file.size)
    # listname = file.name.split('.')  #自定义修改文件名 可用账户ID或者日期时间拼接文件名 防止文件名发生冲突
    # print(listname[len(listname)-1])
    # file.name = 'cq'+ '.' + listname[len(listname)-1]
    # print(file.name)

    # path = os.path.join(settings.MDEIA_ROOT,file.name) # 文件存储的目标路径 拼接路径

    #日期目录
    myDate =datetime.today().strftime("%Y/%m/%d")
    path = os.path.join(settings.MDEIA_ROOT,myDate)
    print(path)
    if not os.path.exists(path):
        os.makedirs(path) #可以递归创建子目录
    #文件的绝对路径
    path = os.path.join(path,file.name)
    with open(path,'wb') as fp:
        if file.multiple_chunks(): #如果文件大于2.5M 分片读写
            for chip in file.chunks():
                fp.write(chip)
        else:
            fp.write(file.read())



    print(path)


    return HttpResponse('hhah')


def yzm(request):
    vc = VerifyCode()
    res = vc.output()
    request.session['code'] = vc._code
    print(vc._code)
    return HttpResponse(res,'image/png')


def login(request):
    return render(request,'app/login.html')


def dologin(request):
    yzm = request.POST.get('yzm')
    code = request.session.get('code')
    if yzm == code:
        return HttpResponse('验证成功')
    return HttpResponse('验证失败')


def userlist(request,num='1'):
    user = User.objects.all()
    current = int(num)
    print(current)
    paginator = Paginator(user,4)
    print(paginator.num_pages)
    page = paginator.page(current)
    if paginator.num_pages > 10:
        if current-5 <= 0:
            coustomRange = range(1,11)
        elif current + 5 > paginator.num_pages:
            coustomRange = range(paginator.num_pages-9,paginator.num_pages+1)
        else:
            coustomRange = range(current-5,current+5)
    else:
       coustomRange = paginator.page_range
    dic = {
        'users':page.object_list,
        'page_range': coustomRange,
        'page':page,
    }

    return render(request,'app/userlist.html',context=dic)


def adduser(request):
    user = User()
    user.uname = '一缕星光' + str(randint(1,454554))
    hash = hashlib.md5()
    hash.update(str(randint(10000,99999)).encode('utf-8'))
    user.password = hash.hexdigest()
    print(user.password)
    user.uage = randint(18,26)
    user.save()
    return HttpResponse("添加用户成功%d" %user.id)