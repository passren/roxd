from django.conf.urls import include, url
from django.contrib import admin
from roxd import views as roxd_views
from track import urls as track_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', roxd_views.index, name='home_page'),
    url(r'^track/', include(track_urls)),
]
