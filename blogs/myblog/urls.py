from django.conf.urls import url

from myblog import views

urlpatterns = [
    url(r'^index/$',views.blog,name='index'), #博客前台首页
    url(r'^index/(\d+)/$',views.blog,name='index1'),#博客分页
    url(r'^showblog/(\d+)/$',views.showblog,name='showblog'), #博客详情
    url(r'^submitcomment/$',views.submitcomment,name='submitcomment')

]