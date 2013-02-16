from django.conf.urls.defaults import *

urlpatterns = patterns('geoproject.views',
    (r'^$', 'index'),
    (r'^list$', 'list'),

)