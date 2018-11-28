from django.conf.urls import url

from blogs import views

urlpatterns = [
    url(r'^index/$', views.index, name='index')
]
