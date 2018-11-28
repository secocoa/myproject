from django.conf.urls import url

from two import views
urlpatterns = [
    url(r'addteam/',views.addteam),
    url(r'addgroup/',views.addgroup),
    url(r'deleteteam/$',views.delete_team),
    # url(r'^findgroup/$',views.findgroup),
]
