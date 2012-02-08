from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'homepage.views.index', name='home_index'),

)
