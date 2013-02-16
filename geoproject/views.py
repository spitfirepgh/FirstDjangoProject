from geoproject.models import SnowZone,BrokenMeter
from django.shortcuts import render_to_response
from django.utils.safestring import SafeString
from vectorformats.Formats import Django, GeoJSON
import json


def index(request):
    snow_zone = []
    broken_meter = []
    geoj = GeoJSON.GeoJSON()
    djf = Django.Django(geodjango='mpoly', properties=['name'])
    snow_zone = geoj.encode(djf.decode(SnowZone.objects.all()))
    djf = Django.Django(geodjango='pnt', properties=['name'])
    broken_meter = geoj.encode(djf.decode(BrokenMeter.objects.all()))
    return render_to_response('geoproject/mapview.html', {'snow_zones': SafeString(snow_zone),'broken_meter': SafeString(broken_meter)})

def list(request):
    snow_zone = SnowZone.objects.all()
    broken_meter = BrokenMeter.objects.all()
    return render_to_response('geoproject/listview.html', {'snow_zones': snow_zone,'broken_meter': broken_meter})
