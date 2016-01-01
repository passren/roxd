from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Gpx)
admin.site.register(models.Route)
admin.site.register(models.Track)
admin.site.register(models.Waypoint)
admin.site.register(models.Gpx_Route_Rel)
admin.site.register(models.Gpx_Track_Rel)
admin.site.register(models.Gpx_Waypoint_Rel)
admin.site.register(models.Route_Waypoint_Rel)
admin.site.register(models.Track_Waypoint_Rel)