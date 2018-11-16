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