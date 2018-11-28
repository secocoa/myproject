from random import randint

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from two.models import Team, Group


def addteam(request):
    team = Team(tname=str(randint(1801, 1807)))
    team.save()
    return HttpResponse('增加班级')


def addgroup(request):
    g1 = Group(gname='起的隆冬强'+str(randint(1,100)))
    g1.team = Team.objects.last()
    g1.save()
    return HttpResponse("增加小组")

def delete_team(request):
    #外键设置为DO_NOTHING,从表中有记录的班级无法删除
    team  = Team.objects.first()
    team.delete()
    return HttpResponse('删除班级')

#正向查询
def find_group(requeset):
    team = Team.objects.first()
    print(team.group_set.all())
    return  HttpResponse("查询成功")
# 反向查询
 def lookup_group(request):
     team = Team.objects.filter(pk=6)
     print(team.group.team_id)
     return  HttpResponse('查询成功')
