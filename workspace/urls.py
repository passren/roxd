from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='workspace_index'),
    url(r'roads/$', views.roads, name='workspace_roads'),
    url(r'favorite/$', views.index, name='workspace_favorite'),
    url(r'followed/$', views.index, name='workspace_followed'),
    url(r'messages/$', views.index, name='workspace_messages'),
    url(r'analysis/$', views.index, name='workspace_analysis'),
]
