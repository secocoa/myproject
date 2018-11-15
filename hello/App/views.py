from django.shortcuts import render,HttpResponse

# Create your views here.
from App.models import User, Goods


def index(req):
    return render(req,'index.html')

def hello(req):

    res = User.objects.all()
    return render(req,'hello.html',context={'data':res})
def addgoods(req):
    user = User(username='蔡强',userpasswd='23')
    user.save()
    good = Goods(goodname='大盘鸡',userid=user)
    good.save()
    return HttpResponse('添加商品成功')