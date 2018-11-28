from django.conf.urls import url, include
from ajax import  views

urlpatterns = [
    url(r'^register/$',views.register,name='register'),

]
