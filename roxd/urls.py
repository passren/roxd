from django.conf.urls import include, url
from django.contrib import admin
from roxd import views as roxd_views
from track import urls as track_urls
from member import views as member_views
from workspace import urls as workspace_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', roxd_views.index, name='home'),
    
    url(r'^track/', include(track_urls)),
    url(r'^workspace/', include(workspace_urls)),
    
    url(r'^signup/', member_views.signup, name='signup'),
    url(r'^signin/', member_views.signin, name='signin'),
    url(r'^logout/', member_views.logout, name='logout'),
    url(r'^profile/(?P<username>\w+/$)', member_views.profile, name='profile'),
]
