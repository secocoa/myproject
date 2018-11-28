from django.conf.urls import url

from mycookie import views

urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url(r'^login/$',views.login,name='login'),
    url(r"^register/$",views.register,name='register'),
    url(r'^logout/$', views.logout1, name='logout'),


]
