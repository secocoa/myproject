from random import randint

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import Student, Archive


def addstudent(request):
    list1 = ['张','李','赵','顾','夏']
    list2 = ['雪','峰','军','国','辉']
    student = Student()
    student.sname = list1[randint(0,4)] + list2[randint(0,4)]
    student.save()
    return HttpResponse('学生%d添加成功'% student.id)

def addarchive(req):
    archive = Archive()
    archive.phone = str(randint(100000000,1000000000))
    archive.student = Student.objects.get(pk=randint(1,Student.objects.count()))
    archive.save()
    return HttpResponse('增加学生档案%d'% archive.id)

#删除学生
def deletestudent(req):
    try:
        student = Student.objects.get(pk=3) #PROTECT 从表与主表数据有关联时无法删除主表数据
        student.delete()
    except Exception as e:
        print(e)
        return  HttpResponse('学生不存在')
    return  HttpResponse('学生删除成功')

#正向查询 由主表查从表
def get_archive_by_student(req):
    student = Student.objects.get(pk=3)
    print(student.archive)    #从表是类名的小写

    return HttpResponse(student.archive)

#反向查询 由从表查主表
def getstudent(req):
    archive = Archive.objects.get(pk=1)
    print(archive)
    print(archive.student) #主表名是类名的小写
    return HttpResponse(archive.student)

#跨关系查询
def loopup(req):
    #根据学生查档案
    archive = Archive.objects.filter(student__sname='李辉')
   #根据档案查学生
    student = Student.objects.filter(archive__phone=159267107)
    return HttpResponse(archive)

