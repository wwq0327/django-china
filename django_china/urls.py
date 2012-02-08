from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_china.views.home', name='home'),
    # url(r'^django_china/', include('django_china.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
                        url(r'^accounts/', include('profiles.urls')),
                        url(r'^$', include('homepage.urls')),

)
media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
urlpatterns += patterns('',
                        (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
                         {
                             'document_root': settings.MEDIA_ROOT,
                             }),
                        )
