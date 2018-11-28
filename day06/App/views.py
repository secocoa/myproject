
from random import randint
import json as myjson

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from App.models import Team, Student


def index(request):
    return HttpResponse('页面成功')

def add_team(request):
    team = Team(tname=str(randint(1801,1810)))
    team.save()
    return  HttpResponse('创建班级%d' % team.id)

def add_student(req):
    student = Student(sname='哈喽树先生%d' % randint(1,1000))
    student.team = Team.objects.get(pk= randint(1,Team.objects.count()))
    student.save()
    return HttpResponse('创建学生%d' % student.id)


#班级列表
def list_team(request):
    teams = Team.objects.all()
    return render(request,'teamList.html',context={'data':teams})

#除了第一个参数request其余的参数个数应该和模式中组的个数一一对应
def studentlist(request,num):
#从模式中获取的都是字符串
    stus = Student.objects.filter(team_id=int(num))
    print(stus)
    return render(request,'student.html',context={'data':stus})


# def studentlist(request,tname,num):
# #从模式中获取的都是字符串
#     return HttpResponse(tname + '-----' +  num)

#如果视图函数匹配的是命名组，则除去第一个request之外，其他参数必须和组名一致
def studentlist2(request,tid):
    return HttpResponse(tid)


def requestlist(request):
    #请求类型
    print(request.content_type)
    #GET参数，是一个字典
    print(request.GET)
    #请求路径
    print(request.path)
    #请求协议
    print(request.scheme)
    #请求的方法
    print(request.method)
    #请求头的源信息
    #print(request.META)
    s1 = '<li>'
    for key in request.META:
        s1 += str(key) + '----' + str(request.META[key]) + "</li><li>"
    s1 = s1.rstrip("<li>")
    return HttpResponse(s1)

    #常用方法
    # print(request.get_host())
    # print(request.get_full_path())
    # print(request.build_absolute_uri())
    # print(request.is_ajax())
    # return HttpResponse('请求对象')

#显示学生注册页面
def show_register(request):
    return render(request,'students.html')


def regiser(request):
    if request is 'GET':
        print('GET')
        print(request.GET)
        #获取单个值
        sname = request.GET.get('sname')

        #获取多个值
        hobby  = request.GET.getlist('hobby')
        print(sname)
        print(hobby)

        #成员判断
        if 'team' in request.GET:
            print("存在")
        for key,value in request.GET.items():
            print(key,'----',value)
        return HttpResponse('学生注册')
    else:
        print('POST')
        print(request.POST)
        return  HttpResponse('post学生注册')

def hello(request):
    #1.返回一个字符串
    response = HttpResponse()
    response.content = '大家好,今天天不错'.encode('utf8')
    response.status_code = 200
    response.charset = 'utf-8'
    response.content_type = 'text/html'
    return  response
    #  return HttpResponse("wwed")

    #2.返回一个模板
    # response = render(request,'student.html')
    # response.status_code = 200
    # print(response)
    # print(response.content.decode('utf8'))
    # return  response


def processjson(request):
    # 1 使用JsonResponse返回json数据
    # person = {'name':'马云','age':21,'sex':'男'}
    # return JsonResponse(person)

    #2 使用系统内置json
    # res = myjson.dumps([1,2,3,4])
    # return HttpResponse(res)

    #3 将QuerySet转换呢为json
    # stus = Student.objects.all()
    # print(list(stus.values()))
    # res = {'data':list(stus.values())}
    # return JsonResponse(res)

    stu = Student.objects.all()
    res = myjson.dumps(list(stu.values()))
    print(type(res))
    return HttpResponse(res)


def chong(request,num):
    # return HttpResponseRedirect('/App/')
    # return redirect("/App/")s

    #带参数,硬编码
    # return redirect('/App/studentlist/2/')
    #return redirect('/App/studentlist/%s' % num)

    #反向解析 通过namespace:name 获得url
    #url带位置参数（无命名的值）
    # res = reverse('App:studentlist',args=(num))
    # return  redirect(res)

    #有命名的关键字参数
    res = reverse("App:studentlist2",kwargs={'tid':num})
    print(res)
    return redirect(res)