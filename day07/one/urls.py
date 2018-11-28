from django.conf.urls import url

from one import views

urlpatterns = [
    # url(r'^index/$',views.index,name='index')
    url(r'addstudent/$',views.add_student,name='addstudent'),
    # 模板语法
    url(r'^muban/$', views.muban, name='muban'),
    url(r'^label/$',views.label,name='label'),
    url(r'^include/$',views.includehtml,name='includehtml'),
    url(r'^base/$',views.base,name='base'),
    url(r'^child/$',views.child,name='child')
]
