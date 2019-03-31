from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.home, name='home'),
    url(r'^projects$', views.projects, name='projects'),
    url(r'^projects/create$', views.project_create, name='project_create'),
    url(r'^register$', views.register, name='register'),
    url(r'^register_user$', views.register_user, name='register_user'),
    url(r'^login$', views.login, name='login'),
    url(r'^login_user$', views.login_user, name='login_user'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^projects/(?P<project_id>[0-9]+)$', views.project_detail, name='projects_detail'),
    url(r'^projects/(?P<project_id>[0-9]+)/update', views.project_update, name="project_update"),
    url(r'^projects/(?P<project_id>[0-9]+)/delete', views.project_delete, name="project_delete"),
    url(r'^projects/(?P<project_id>[0-9]+)/add_member', views.project_add_member, name="project_add_member")

]