from random import randint

from django.db.models import Count, Q, F
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import Student, Course


def addstudent(req):
    student = Student()
    student.sno = '1806' + str(randint(1,10000))
    student.sname = '栋梁' + str(randint(1,10000))
    student.ssex = '男' if randint(1,2) % 2 else '女'
    student.sclass = '1806'
    student.save()
    return HttpResponse('创建一个学生成功%d'%student.id)


def getoneobject(request):
    # stu = Student.objects.get(pk=1)
    # stu = Student.objects.get(sage=10) #get 只能获取一个对象
    #返回多个对象会报错误 MultipleObjectsReturned
    # 也不能返回空的 会报DoesNotExist
    # try:
    #     stu = Student.objects.get(sage=10)
    #     print(stu)
    # except Exception as e :
    #     print(e)
    #     return HttpResponse('学生信息不存在')
    # return HttpResponse(stu.sname)

    # 2 first()获取第一个记录 last获取最后一条记录
    # stu = Student.objects.first()
    # return HttpResponse(stu.sno + " " + stu.sname)

    #3 count()获取记录个数
    # res = Student.objects.count()
    # res = Student.objects.filter(sage=0.).count()
    # return HttpResponse('共有 %d ' % res)

    #4 exists()判断查询集中有没有记录
    res = Student.objects.exists()
    if res:
        return HttpResponse('有记录')
    else:
        return HttpResponse('空记录')


#限制结果集 支持返回查询集的过滤器
def limitset(req):
    stus = Student.objects.all()[::2] #select * from student limit 2 切片动作
    #切片可以 但是不支持负索引 切片返回的是一个集合
    # return render(req,'student.html',context={'data':stus})

    #索引 索引返回的是一个对象
    stus = Student.objects.all()[3]
    return render(req,'student.html',context={'data':[stus]})


def fieldquery(req):
    # 1 iexact 不区分大小写精确匹配
    # stu = Student.objects.filter(sname__exact='admin')

    # 2 icontains 包含,相当于 like '%data%'
    # stu = Student.objects.filter(sname__icontains='栋梁')

    # 3 startwith 以‘’‘为开头的
    # stu = Student.objects.filter(sname__startswith='栋')

    # 4 isnull 等价于 select * from student where sage is null
    # stu = Student.objects.filter(sage__isnull=True)

    # 5 关系运算 select * from student where id>2 and id<6
    # stu = Student.objects.filter(id__gt=2,id__lt=6)

    # 6 in  集合运算
    # stu = Student.objects.filter(id__in=[1,4,6])
    # stu = Student.objects.filter(id__in=(1,4,6))
    # in后可以跟子查询,但子查询只能返回一个字段
    # sub = Student.objects.filter(id__lte=5).values('id')
    # stu = Student.objects.filter(id__in=sub)

    # 7 regex 正则查询
    # python支持utf8,python正则规则中/d不表示纯数字,要表示纯数字要用[0-9]
    stu = Student.objects.filter(sname__regex=r'[0-9]+$')
    print(stu.query)
    return  render(req,'student.html',context={'data':stu})



def groupby(req):
    # 统计Max,Min,Count,Sum,Avg
    # select max(id),min(id),avg(id) from student
    # maxid = Student.objects.aggregate(Max('id'))
    # minid = Student.objects.aggregate(Min('id'))
    # avgid = Student.objects.aggregate(Avg('id'))
    # return HttpResponse("max={} min={} avg={}".format(maxid,minid,avgid)


    #分组统计 返回的是QuerySet
    #使用values进行分组，使用annotate统计
    res = Student.objects.values('ssex').annotate(Count('id'))
    return HttpResponse(res)


#Q对象和F对象
def QandF(req):
    #逻辑或 |
    #select * from student where id=2 or id=3
    # stu = Student.objects.filter(Q(id__gte=2) | Q(id__lte=5))
    #逻辑与 &
    # stu = Student.objects.filter(Q(id__gte=2) & Q(id__lte=5))
    # 逻辑取反 ~
    # stu = Student.objects.filter(~Q(id__gte=2))

    #F对象， 表示表中两列的对比
    stu =Student.objects.filter(sage__gt=F('id'))
    return  render(req,'student.html',context={'data':stu})


def addcourse(req):
    course = Course(cname='python从入门到放弃'+str(randint(1,100)),ccredit=4)
    course.save()
    return HttpResponse('增加一门新课程%d' %course.id)


def getcourse(req):
    #自定义管理器对象后 就不能再使用objects
    course = Course.cmanager.all()
    print(course)
    course = Course.gmanager.all()
    print(course)

    return HttpResponse('获取课程')

