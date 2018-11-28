from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^adduser/$', views.adduser, name='adduser'),
    url(r'^register/$', views.register, name='register'),

    url(r'^homework/', views.homework, name='homework'),
    url(r'^checkusername/$', views.checkusername, name='checkusername'),

    url(r'^index/$', views.index, name='index'),
    url(r'^login/$',views.login,name='login'),

    #验证代码
    url(r'^send/$',views.send,name='send'),
    url(r'^dologin/$',views.dologin,name='dologin')
]
