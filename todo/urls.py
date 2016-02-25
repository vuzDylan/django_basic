from django.conf.urls import url
from todo import views

urlpatterns = [
    url(r'^all/$', views.view_todos),
    url(r'^completed/$', views.view_completed),
    url(r'^uncompleted/$', views.view_uncompleted),
    url(r'^create/$', views.create_todo),
    url(r'^toggle/(?P<post_id>\d+)/$', views.toggle_todo),
]
