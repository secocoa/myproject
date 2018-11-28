from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^index/',views.index,name='index'),
    url(r'^upload/',views.upload,name='upload'),
    url(r'^doupload/',views.doupload,name='doupload'),
    #验证码
    url(r'^verifycode/$',views.yzm,name='yzm'),# 返回验证码图片
    url(r'^login/$',views.login,name='login'), # login.html的路由
    url(r'^dologin/$',views.dologin,name='dologin'),#提交表单 通过session中的验证码与输入框的value对比 验证输入

    #分页
    url(r'^userlist/$',views.userlist,name='userlist'),
    url(r'^userlist/(\d+)/$',views.userlist,name='userlist1'),
    url(r'^adduser/$',views.adduser,name='user'),
]
