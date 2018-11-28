from django.conf.urls import url

from App import views

urlpatterns = [
    # url(r'^$',views.index),
    url(r'^addteam/$',views.add_team,name='addstudent'),
    url(r'^addstudent/$',views.add_student,name='addteam'),
    url(r'^teamlist/$',views.list_team,name='teamlist'),
    #动态URL解析
    url(r'^studentlist/(\d+)/$',views.studentlist,name='studentlist'),
   # url(r'^studentlist/(/w)/(\d+)/$',views.studentlist,name='studentlist')
    #命名组
    url(r'^studentlist2/(?P<tid>\d+)/$', views.studentlist2, name='studentlist2'),


    #request对象

    url(r'^req/$',views.requestlist,name='req'),

    #get post
    url(r'^getstudent/$',views.show_register,name='showregister'),
    url(r'^register/$',views.regiser,name='register'),
    #response
    url(r'^hello/$',views.hello,name='hello'),
    url(r'^json/$',views.processjson,name='processjson'),

    #重定向
    url(r'^cdx/(\d+)/$',views.chong,name='cdx'),
    # url(r'^cdx2/$',views.chong2,name='cdx2')

]
