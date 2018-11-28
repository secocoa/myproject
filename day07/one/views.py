from random import randint

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from one.models import Student


def add_student(request):
    stu = Student()
    stu.sname = '小明' + str(randint(1,10000))
    stu.ssex = randint(0,1)
    stu.sage = randint(18,22)
    stu.save()
    return HttpResponse('创建学生%d' % stu.id)


# def index(request):
#     # return HttpResponse('首页')
#     # template = loader.get_template('app/index.html')
#     # print(template)
#     # res = template.render()
#     # print(res)
#     # return HttpResponse(res)



def login(request):
    return HttpResponse('登录页面')

#模板语法
def muban(request):
    a = 10
    b = 'hello'
    c = [1,2,3,4]
    d = {'a1':20,'b1':40,'c1':60}
    stu  = Student.objects.all()
    return  render(request,'app/muban.html',context={'a':a,
                                                     'b':b,'c':c,
                                                     'd':d,'stu':stu})

def label(request):
    stu = Student.objects.all()
    l1 = [1,2,3,4]
    return  render(request,'app/label.html',context={'stu':stu,
                                                    })


def includehtml(request):
    return  render(request,'app/include.html')


def base(request):
    return render(request,'app/base.html')

def child(req):
    return HttpResponse('child')
