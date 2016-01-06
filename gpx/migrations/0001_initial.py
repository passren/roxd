# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-06 12:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gpx',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('version', models.CharField(blank=True, max_length=50)),
                ('creator', models.CharField(blank=True, max_length=50)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('desc', models.CharField(blank=True, max_length=255)),
                ('author', models.CharField(blank=True, max_length=50)),
                ('copyright', models.CharField(blank=True, max_length=100)),
                ('link', models.CharField(blank=True, max_length=255)),
                ('time', models.DateTimeField(null=True)),
                ('keywords', models.CharField(blank=True, max_length=255)),
                ('bounds_minlat', models.DecimalField(decimal_places=10, default=0, max_digits=19, null=True)),
                ('bounds_minlon', models.DecimalField(decimal_places=10, default=0, max_digits=19, null=True)),
                ('bounds_maxlat', models.DecimalField(decimal_places=10, default=0, max_digits=19, null=True)),
                ('bounds_maxlon', models.DecimalField(decimal_places=10, default=0, max_digits=19, null=True)),
                ('extensions', models.TextField(blank=True)),
                ('origial_xml', models.TextField(blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_updated_date', models.DateTimeField(auto_now=True)),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gpx_create_user_id', to=settings.AUTH_USER_MODEL)),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gpx_update_user_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Gpx_Route_Rel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('gpx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gpx.Gpx')),
            ],
        ),
        migrations.CreateModel(
            name='Gpx_Track_Rel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('gpx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gpx.Gpx')),
            ],
        ),
        migrations.CreateModel(
            name='Gpx_Waypoint_Rel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('gpx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gpx.Gpx')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('cmt', models.CharField(blank=True, max_length=255)),
                ('desc', models.CharField(blank=True, max_length=255)),
                ('src', models.CharField(blank=True, max_length=50)),
                ('link', models.CharField(blank=True, max_length=255)),
                ('number', models.IntegerField(null=True)),
                ('type', models.CharField(blank=True, max_length=50)),
                ('extensions', models.TextField(blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_updated_date', models.DateTimeField(auto_now=True)),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_create_user_id', to=settings.AUTH_USER_MODEL)),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_update_user_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Route_Waypoint_Rel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gpx.Route')),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('cmt', models.CharField(blank=True, max_length=255)),
                ('desc', models.CharField(blank=True, max_length=255)),
                ('src', models.CharField(blank=True, max_length=50)),
                ('link', models.CharField(blank=True, max_length=255)),
                ('number', models.IntegerField(null=True)),
                ('type', models.CharField(blank=True, max_length=50)),
                ('extensions', models.TextField(blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_updated_date', models.DateTimeField(auto_now=True)),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='track_create_user_id', to=settings.AUTH_USER_MODEL)),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='track_update_user_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Track_Waypoint_Rel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gpx.Track')),
            ],
        ),
        migrations.CreateModel(
            name='Waypoint',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lat', models.DecimalField(decimal_places=10, max_digits=19)),
                ('lon', models.DecimalField(decimal_places=10, max_digits=19)),
                ('ele', models.DecimalField(decimal_places=10, default=0, max_digits=19, null=True)),
                ('time', models.DateTimeField(null=True)),
                ('magvar', models.DecimalField(decimal_places=10, default=0, max_digits=19, null=True)),
                ('geoidheight', models.DecimalField(decimal_places=10, default=0, max_digits=19, null=True)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('cmt', models.CharField(blank=True, max_length=255)),
                ('desc', models.CharField(blank=True, max_length=255)),
                ('src', models.CharField(blank=True, max_length=50)),
                ('link', models.CharField(blank=True, max_length=255)),
                ('sym', models.CharField(blank=True, max_length=50)),
                ('type', models.CharField(blank=True, max_length=50)),
                ('fix', models.CharField(blank=True, max_length=10)),
                ('sat', models.IntegerField(null=True)),
                ('hdop', models.DecimalField(decimal_places=10, default=0, max_digits=19, null=True)),
                ('vdop', models.DecimalField(decimal_places=10, default=0, max_digits=19, null=True)),
                ('pdop', models.DecimalField(decimal_places=10, default=0, max_digits=19, null=True)),
                ('ageofdgpsdata', models.DecimalField(decimal_places=10, default=0, max_digits=19, null=True)),
                ('dgpsid', models.IntegerField(null=True)),
                ('extensions', models.TextField(blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_updated_date', models.DateTimeField(auto_now=True)),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waypoint_create_user_id', to=settings.AUTH_USER_MODEL)),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waypoint_update_user_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='track_waypoint_rel',
            name='waypoint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gpx.Waypoint'),
        ),
        migrations.AddField(
            model_name='route_waypoint_rel',
            name='waypoint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gpx.Waypoint'),
        ),
        migrations.AddField(
            model_name='gpx_waypoint_rel',
            name='waypoint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gpx.Waypoint'),
        ),
        migrations.AddField(
            model_name='gpx_track_rel',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gpx.Track'),
        ),
        migrations.AddField(
            model_name='gpx_route_rel',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gpx.Route'),
        ),
    ]
