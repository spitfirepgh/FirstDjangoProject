from django.contrib.gis import admin
from models import SnowZone,BrokenMeter

admin.site.register(SnowZone, admin.OSMGeoAdmin)
admin.site.register(BrokenMeter, admin.OSMGeoAdmin)