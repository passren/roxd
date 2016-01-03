from django.conf.urls import include, url
from django.contrib import admin
from roxd import views as roxd_views
from track import urls as track_urls
from member import views as member_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', roxd_views.index, name='home'),
    url(r'^track/', include(track_urls)),
    url(r'^signin/', member_views.signin, name='signin'),
    url(r'^logout/', member_views.logout, name='logout'),
]
