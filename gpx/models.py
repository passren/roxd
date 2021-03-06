from django.db import models
from django.contrib.auth.models import User

# Models of GPX object
class Gpx(models.Model):
    id = models.AutoField(primary_key=True)
    version = models.CharField(max_length=50, blank=True)
    creator = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50, blank=True)
    desc = models.CharField(max_length=255, blank=True)
    author = models.CharField(max_length=50, blank=True)
    copyright = models.CharField(max_length=100, blank=True)
    link = models.CharField(max_length=255, blank=True)
    time = models.DateTimeField(null=True)
    keywords = models.CharField(max_length=255, blank=True)
    bounds_minlat = models.DecimalField(max_digits=19, decimal_places=10, null=True, default=0)
    bounds_minlon = models.DecimalField(max_digits=19, decimal_places=10, null=True, default=0)
    bounds_maxlat = models.DecimalField(max_digits=19, decimal_places=10, null=True, default=0)
    bounds_maxlon = models.DecimalField(max_digits=19, decimal_places=10, null=True, default=0)
    extensions = models.TextField(blank=True)
    origial_xml = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    create_user = models.ForeignKey(User, null=False, related_name='gpx_create_user_id')
    last_updated_date = models.DateTimeField(auto_now=True)
    update_user = models.ForeignKey(User, null=False, related_name='gpx_update_user_id')
    
class Route(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    cmt = models.CharField(max_length=255, blank=True)
    desc = models.CharField(max_length=255, blank=True)
    src = models.CharField(max_length=50, blank=True)
    link = models.CharField(max_length=255, blank=True)
    number = models.IntegerField(null=True)
    type = models.CharField(max_length=50, blank=True)
    extensions = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    create_user = models.ForeignKey(User, null=False, related_name='route_create_user_id')
    last_updated_date = models.DateTimeField(auto_now=True)
    update_user = models.ForeignKey(User, null=False, related_name='route_update_user_id')
    
class Track(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    cmt = models.CharField(max_length=255, blank=True)
    desc = models.CharField(max_length=255, blank=True)
    src = models.CharField(max_length=50, blank=True)
    link = models.CharField(max_length=255, blank=True)
    number = models.IntegerField(null=True)
    type = models.CharField(max_length=50, blank=True)
    extensions = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    create_user = models.ForeignKey(User, null=False, related_name='track_create_user_id')
    last_updated_date = models.DateTimeField(auto_now=True)
    update_user = models.ForeignKey(User, null=False, related_name='track_update_user_id')
    
class Waypoint(models.Model):
    id = models.AutoField(primary_key=True)
    lat = models.DecimalField(max_digits=19, decimal_places=10, null=False)
    lon = models.DecimalField(max_digits=19, decimal_places=10, null=False)
    ele = models.DecimalField(max_digits=19, decimal_places=10, null=True, default=0)
    time = models.DateTimeField(null=True)
    magvar = models.DecimalField(max_digits=19, decimal_places=10, null=True, default=0)
    geoidheight = models.DecimalField(max_digits=19, decimal_places=10, null=True, default=0)
    name = models.CharField(max_length=50, blank=True)
    cmt = models.CharField(max_length=255, blank=True)
    desc = models.CharField(max_length=255, blank=True)
    src = models.CharField(max_length=50, blank=True)
    link = models.CharField(max_length=255, blank=True)
    sym = models.CharField(max_length=50, blank=True)
    type = models.CharField(max_length=50, blank=True)
    fix = models.CharField(max_length=10, blank=True)
    sat = models.IntegerField(null=True)
    hdop = models.DecimalField(max_digits=19, decimal_places=10, null=True, default=0)
    vdop = models.DecimalField(max_digits=19, decimal_places=10, null=True, default=0)
    pdop = models.DecimalField(max_digits=19, decimal_places=10, null=True, default=0)
    ageofdgpsdata = models.DecimalField(max_digits=19, decimal_places=10, null=True, default=0)
    dgpsid = models.IntegerField(null=True)
    extensions = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    create_user = models.ForeignKey(User, null=False, related_name='waypoint_create_user_id')
    last_updated_date = models.DateTimeField(auto_now=True)
    update_user = models.ForeignKey(User, null=False, related_name='waypoint_update_user_id')
    
class Gpx_Route_Rel(models.Model):
    id = models.AutoField(primary_key=True)
    gpx = models.ForeignKey(Gpx, null=False)
    route = models.ForeignKey(Route, null=False)
    
class Gpx_Track_Rel(models.Model):
    id = models.AutoField(primary_key=True)
    gpx = models.ForeignKey(Gpx, null=False)
    track = models.ForeignKey(Track, null=False)
    
class Gpx_Waypoint_Rel(models.Model):
    id = models.AutoField(primary_key=True)
    gpx = models.ForeignKey(Gpx, null=False)
    waypoint = models.ForeignKey(Waypoint, null=False)
    
class Route_Waypoint_Rel(models.Model):
    id = models.AutoField(primary_key=True)
    route = models.ForeignKey(Route, null=False)
    waypoint = models.ForeignKey(Waypoint, null=False)
    
class Track_Waypoint_Rel(models.Model):
    id = models.AutoField(primary_key=True)
    track = models.ForeignKey(Track, null=False)
    waypoint = models.ForeignKey(Waypoint, null=False)