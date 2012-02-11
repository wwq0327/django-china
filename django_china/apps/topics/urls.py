from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'topics.views.index', name='tc_index'),
                       url(r'^create/$', 'topics.views.create', name='tc_create'),
                       url(r'^(?P<t_pk>\d+)/edit/$', 'topics.views.topic_edit', name="tc_edit"),
                       url(r'^(?P<tc_pk>\d+)/$', 'topics.views.topic_detail', name='tc_detail'),
                       url(r'^node(?P<node_pk>\d+)/$', 'topics.views.node_topics', name='tc_node'),

)
