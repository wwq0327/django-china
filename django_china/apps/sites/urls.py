from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'sites.views.index', name='sites_index'),
                       url(r'^create/$', 'sites.views.create', name='sites_create'),

)
