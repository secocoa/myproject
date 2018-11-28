import json
import os
import base64
from random import randint
from bs4 import BeautifulSoup

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from adminmanage.models import User, Category, Blog, Label
from adminmanage.myhelper import Mymd5
from adminmanage.sms import SMS
from blogs import settings
from itertools import chain


def index(request):
    listout = []
    blogs = Blog.bmymanager.all()
    for blog in blogs:
        list1 = []  # 第一个列表存放每一次迭代出来的数据
        category = blog.category
        comment = blog.comments_set.count()
        print(comment)
        labels = blog.label.all()
        list1.append(blog)
        list1.append(labels)
        list1.append(comment)
        listout.append(list1)
        print(list1)
    print(listout)
    return render(request,'adminmanage/index.html',context={'blogs':blogs,'listout':listout})


def base(request):
    return render(request,'adminmanage/base.html')


def login(request):
    if request.method == 'GET':
        return render(request,'adminmanage/login.html')
    else:
            uname = request.POST.get('login')
            password = request.POST.get('pwd')
            phone = request.POST.get('phone')
            code = request.session.get('yzm')
            print(password)
            print(type(password))
            password = Mymd5(password).encrypt()
            try:
                user = User.umanager.get(uname=uname)
                print(user.password)
            except Exception as e :
                return render(request,'notice.html',context={
                'msg': '用户名或者密码错误',
                'code': '-1',
                'wait': 2,
                'url' : reverse('myManage:login')
            })
            if password == user.password and phone == user.phone and  request.POST.get('yzm') == code:
                request.session['uname'] = uname #session 中加入名字
                return render(request,'adminmanage/index.html')
            else:
                return render(request,'notice.html',context={
                'msg': '用户名或者密码错误',
                'code': '-1',
                'wait': '3',
                'url' : reverse('myManage:login')
            })

def register(request):
    return render(request,'adminmanage/regiter.html')

def verifylogin(request):
    uname  = request.POST.get()

def verifyregister(request):
    print(type(request.session.get('yzm')))
    print(type(request.POST.get('yzm')))
    if request.session.get('yzm') == request.POST.get('yzm'):
        register_user = User()
        uname = request.POST.get('uname')
        password = request.POST.get('pwd')
        phone = request.POST.get('phone')
        mymd5 = Mymd5(password)
        register_user.uname = uname
        register_user.password = mymd5.encrypt()
        print(register_user.password)
        register_user.phone = phone
        register_user.save()
        return redirect(reverse('myManage:index'))
    else:
        return render(request,'notice.html',context={
            'msg':'验证码输入错误或者用户名已被注册',
            'url': reverse('myManage:register'),
            'wait':2,
        })

def send(request):
    phone = request.POST.get('phone')
    print(phone)
    sms = SMS("buildup","SMS_151578255")

    code = randint(1000,9999)
    request.session['yzm'] = str(code)
    res = sms.send_sms(phone,code)
    return HttpResponse(res)


def is_repeat(request):
    uname = request.POST.get('uname')
    csrf = request.POST.get('csrf_token')
    print(uname)
    print(csrf)
    user = User.umanager.filter(uname=uname)
    print(user)
    if user:
        res = {'msg':'用户名已存在'}
        repeat = '0'
    else :
        res = {'msg':'用户名可以使用'}
        repeat = '1'
    res = json.dumps(res)
    request.session['repeat'] = repeat
    return HttpResponse(res)




def write_article(request):
    categorys = Category.cmanager.all()
    data = {
        'categorys':categorys
    }
    return render(request,'adminmanage/add_article.html',context=data)


def save_article(request):
    if 'delete' in request.POST:
        return render(request,'adminmanage/index.html')
    else:
        is_draft = False if 'submit' in request.POST else True
        print(is_draft)
            # 创建博客对象
        blog = Blog()

        title = request.POST.get('title') #获取题目
        print(title)


        #博客内容
        content = request.POST.get('contents')
        print(content)
        uname= request.session.get('uname') # 获取session中的uname 获取用户文件夹
        print(uname)
        abstract_path =os.path.join(settings.MDEIA_ROOT,uname)

        #在用户文件夹下放置富文本发送到服务器的博客 保存为HTML格式
        if not os.path.exists(abstract_path):
            os.makedirs(abstract_path)
        filename = title + '.html'
        filepath= os.path.join(abstract_path,filename)
        with open(filepath,'w',encoding='utf-8') as f :
            f.write(content)
        #将博客路径写入数据库
        #默认摘要
        def_abstract =BeautifulSoup(content,'lxml').get_text()[:50]
        #用户写的摘要
        abstract = request.POST.get('describe')[:50]

        # 获取文章 分类
        category_name = request.POST.get('category')
        print(category_name)

        # 标签
        category = Category.cmanager.get(pk=int(category_name))
        lnames = request.POST.get('tags')
        print(type(lnames))
        list_label = lnames.split(',')
        #获取是否公开
        is_private = request.POST.get('visibility')
        #获取文件图片
        myimage = request.FILES.get('picture')
        modify_name = title + myimage.name
        modify_imagepath = os.path.join(abstract_path, modify_name)
        print(modify_imagepath)
        with open(modify_imagepath, 'wb',) as fp:
            # 如果文件大于２．５Ｍ，分片读写
            if myimage.multiple_chunks():
                for chip in myimage.chunks():
                    fp.write(chip)
            else:
                fp.write(myimage.read())


        #存储数据 准备保存
        blog.btitle =title
        blog.body = filepath
        if abstract:
            blog.abstract = abstract
        else:
            blog.abstract =def_abstract
        print(def_abstract)
        blog.is_prvite = is_private
        blog.is_savedraft = is_draft
        #存储路径
        blog.files = modify_imagepath

        #获取用户id
        user = User.umanager.get(uname=uname)
        #存入
        blog.author_id =user.id
        #存入文章分类
        blog.category_id = int(category_name)
        blog.save()
        this_blog = Blog.bmymanager.get(btitle=title)
        #多对多  获取label
        for label in list_label:
            print(label)  # 循环创建标签对象 将用户所建标签插入label表中
            mylabel = Label()  # 创建标签对象
            mylabel.lname = label
            mylabel.category = category  # 外键
            mylabel.save()
            last_label = Label.lmanager.last()
            this_blog.label.add(last_label)
            blog.save()
            #获取标签表中数据
        msg = '博客发布成功' if is_draft==False else '博客草稿保存成功'
        return render(request,'notice.html',context={
            'msg': msg,
            'wait': 3,
            'code': 1,
            'url':reverse('myManage:index')
        })

#修改博客
def update_article(request,id):
    category = Category.cmanager.all()
    print(type(id))
    print(request.path)
    if request.method == 'GET':
        return render(request,'adminmanage/update-article.html',context={'categorys':category,'tid':id})
    else:
        title = request.POST.get('title')  # 获取题目
        blog =Blog.bmymanager.get(pk=int(id)) #找到修改的博客
        if Blog.bmymanager.filter(btitle=title).count() > 1:
            return render(request,'notice.html',context={
            'msg': '博客中已存在相同题目的博客',
            'wait': 3,
            'url' : request.path,
        })

        blog.label.clear() #接触与此博客有关的所有记录
        #获取页面中修改的数据

        content = request.POST.get('contents') #获取内容
        abstract = request.POST.get('describe')[0:50] #获取摘要
        category_id = request.POST.get('category') #获取文章分类
        category = Category.cmanager.get(pk=int(category_id))
        lnames = request.POST.get('tags') #获取标签
        list_label = lnames.split(',')
        # 获取是否公开
        is_private = request.POST.get('visibility')
        myimage = request.FILES.get('picture')#获取图片
        imagepath = blog.files

        if myimage:
            with open(imagepath, 'wb',) as fp:
                # 如果文件大于２．５Ｍ，分片读写
                if myimage.multiple_chunks():
                    for chip in myimage.chunks():
                        fp.write(chip)
                else:
                    fp.write(myimage.read())
        #获取内容存储路径
        bodypath = blog.body
        with open(bodypath,'w',encoding='utf-8') as f :
          f.write(content)
        blog.abstract = abstract
        blog.btitle = title
        blog.is_prvite = is_private
        blog.category.id= int(category_id)
        blog.save()
        for label in list_label:  # 存储标签
            print(label)  # 循环创建标签对象 将用户所建标签插入label表中
            mylabel = Label()  # 创建标签对象
            mylabel.lname = label
            mylabel.category = category
            mylabel.save()
            last_label = Label.lmanager.last()
            blog.label.add(last_label)
            blog.save()
        return render(request,'notice.html',context={
            'msg':'博客编辑成功',
            'wait':3,
            'url':reverse('myManage:index')
        })

#将找到的博客返回到编辑页面
def get_article(request):
    id = int(request.GET.get('id'))
    print(id)
    myline = ''
    blog = Blog.bmymanager.get(pk=id)
    filepath = blog.body
    with open(filepath,'r') as fp:
        body = fp.read()

    print(body)
    abstract = blog.abstract
    category = blog.category.id
    labelstr = ''
    for label_set in blog.label.all():
        labelstr += label_set.lname +','
    print(labelstr)
    imgpath = blog.files.split('blogs')[1]
    print(imgpath)
    prvite = int(blog.is_prvite)
    data = {
        'title': blog.btitle,
        'body':body,
        'abstract': abstract,
        'label': labelstr,
        'category':category,
        'img':imgpath,
        'prvite':prvite
    }
    print(blog.id)
    return JsonResponse(data)