from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
                       url(r'^(?P<username>\w+)/$', 'people.views.index', name='p_index'),

)
