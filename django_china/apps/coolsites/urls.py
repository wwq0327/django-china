from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'coolsites.views.index', name='sites_index'),
                       url(r'^create/$', 'coolsites.views.create', name='sites_create'),

)
