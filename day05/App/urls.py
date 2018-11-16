from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^addstudent/$',views.addstudent),
    url(r'^addarchive/$',views.addarchive),
    url(r'^deletestudent/$',views.deletestudent),
    url(r'^gabs/$',views.get_archive_by_student),
    url(r'^getstudent/$',views.getstudent),
    url(r'^loopup/$',views.loopup),
]
