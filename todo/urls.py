from django.conf.urls import url
from todo import views

urlpatterns = [
    url(r'^all/', views.view_todos),
]
