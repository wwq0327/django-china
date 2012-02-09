from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'topics.views.index', name='tc_index'),
                       url(r'^create/$', 'topics.views.create', name='tc_create'),

)
