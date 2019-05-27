from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^create/team/$', views.create_team, name="create_team"),
    url(r'^team/([0-9]+)/$', views.team_detail, name="team_detail"),
    url(r'^create/role/$', views.create_role, name="create_role"),
    url(r'^add/permssion/$', views.add_permission, name="add_permission"),
]
