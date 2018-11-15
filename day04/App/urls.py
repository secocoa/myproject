from django.conf.urls import url
from App import views

urlpatterns = [
    url(r'^addstudent/$',views.addstudent),
    url(r'^getoneobject/$',views.getoneobject),
    url(r'^limitset/$',views.limitset),
    url(r'fieldquery/$',views.fieldquery),
    url(r'groupby/$',views.groupby),
    url(r'QandF/$',views.QandF),
    url(r'^addcourse/$',views.addcourse),
    url(r'^getcourse/$',views.getcourse),
]
