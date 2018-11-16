from django.conf.urls import url

from two import views
urlpatterns = [
    url(r'addteam/',views.addteam),
    url(r'addgroup/',views.addgroup)
]
