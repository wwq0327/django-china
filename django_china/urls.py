from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       # url(r'^admin/', include(admin.site.urls)),
                       url(r'^comments/', include('django.contrib.comments.urls')),
)

urlpatterns += patterns('',
                        url(r'^accounts/', include('profiles.urls')),
                        url(r'^$', include('homepage.urls')),
                        url(r'^sites/', include('coolsites.urls')),
                        url(r'^wiki/', include('markupwiki.urls')),
                        url(r'^topics/', include('topics.urls')),
                        url(r'^people/', include('people.urls')),

)
media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
urlpatterns += patterns('',
                        (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
                         {
                             'document_root': settings.MEDIA_ROOT,
                             }),
                        )
