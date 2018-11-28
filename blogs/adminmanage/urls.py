from django.conf.urls import url

from adminmanage import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),#博客后台首页
    url(r'^base/$', views.base, name='base'),#博客后台继承页面
    url(r'^login/$', views.login, name='login'),#登录页面
    url(r'^register/$',views.register,name='register'), #注册页面
    url(r'^verifylogin/$',views.verifyregister,name='verifyregister'), #手机验证注册
    url(r'^send/',views.send,name='send'), #手机发送验证
    url(r'^unamerepeat/$',views.is_repeat,name='isrepeat'), #检测用户名是否重复
    url(r'^write_article/$',views.write_article,name='article'), #写博客
    url(r'^save_article/$',views.save_article,name='savearticle'), #博客发布或者保存草稿
    url(r'^update_article/(\d+)/$',views.update_article,name='update_article'), #博客修改
    url(r'^update_article/$',views.update_article,name='update_article'),#博客修改
    url(r'^get_article/$',views.get_article,name='get_article') #修改博客界面 从数据库动态返回修改博客的数据
]