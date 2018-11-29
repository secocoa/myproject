from random import randint

from django.core.paginator import Paginator
from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse

from adminmanage.models import Blog, Comments, User, Visitnum


def blog(request,num='1'):

    uname = request.session.get('name')
    frontblogs = Blog.bmymanager.filter().order_by('vistnums').reverse()
    frontblog = frontblogs[0:3]
    blogs = Blog.bmymanager.all()
    paginator = Paginator(blogs, 3)
    # print(paginator.count,paginator.page_range)

    # 创建分页对象
    current = int(num)
    page = paginator.page(current)
    if paginator.num_pages > 10:
        #　如果当前页码减去5小于0
        if current - 5 <=0:
            customRange = range(1,11)
        elif current + 5 > paginator.num_pages:
            customRange = range( paginator.num_pages - 9,paginator.num_pages + 1)
        else:
            customRange = range(current - 5,current + 5)
    else:
        customRange = paginator.page_range
    return render(request,'myblog/index.html',context={'blogs':page.object_list,
        'pagerange':customRange, # 页码范围
        'page':page,
        'frontblogs':frontblog,
        })


def showblog(request,id):
        uname = request.session.get('uname')
        blog = Blog.bmymanager.get(pk=int(id))
        visitnums = blog.vistnums
        blog.vistnums = visitnums + 1
        blog.save()
        path =request.path
        comments = Comments.commanager.filter(blog_id=int(id))
        bodypath = blog.body.split('blogs')[1]
        data= {
            'blog':blog,
            'comments': comments,
            'content':bodypath,
            'path':path,
        }

        return render(request,'myblog/article.html',context=data)


def submitcomment(request):
    if request.session.get('uname'):
        uid = User.umanager.get(uname=request.session.get('uname')).id
        comment = Comments()
        bid = request.GET.get('bid')
        blog = Blog.bmymanager.get(pk=int(bid))
        commentbody = request.GET.get('comments')
        comment.blog_id = int(bid)
        comment.user_id = uid
        comment.body = comment.body
        comment.save()
        commentnums = blog.commentnums
        blog.commentnums = commentnums + 1
        return JsonResponse({'code':'1'})
    else:
        return redirect(reverse('myManage:login'))