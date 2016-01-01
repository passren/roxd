from django.conf.urls import include, url
from django.contrib import admin
from roxd import views as roxd_views
from gpx import urls as gpx_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', roxd_views.index, name='home_page'),
    url(r'^gpx/', include(gpx_urls)),
]
