# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, Http404, HttpResponseForbidden, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

from topics.models import Node, Topic, user_count, comments_count
from topics.forms import TopicForm

def index(request):
    """酷站首页面"""
    topics = Topic.objects.all() ## site分类
    nodes = Node.objects.all()

    return render_to_response('topics/index.html',
                              {
                                  'topics': topics,
                                  'nodes': nodes,
                                  'user_count': user_count(),
                                  'comments_count': comments_count()
                               },
                              context_instance=RequestContext(request))

def node_topics(request, node_pk):
    nodes = Node.objects.all()
    node = get_object_or_404(Node, pk=node_pk)
    topics = node.topic_set.all()

    return render_to_response('topics/index.html',
                              {'nodes': nodes,
                               'topics': topics,
                               'is_node': node,

                               },
                              context_instance=RequestContext(request))

@login_required
def create(request):
    """登录用户可自行添加相关网站"""

    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            model = form.save(request.user)
            return HttpResponseRedirect(model.get_absolute_url())
    else:
        form = TopicForm()

    return render_to_response('topics/create.html',
                              {'form': form},
                              context_instance=RequestContext(request))
@login_required
def topic_edit(request, t_pk):
    topic = get_object_or_404(Topic, pk=t_pk)

    if request.user != topic.creater:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = TopicForm(instance=topic, data=request.POST)
        if form.is_valid():
            model = form.save(request.user)
            return HttpResponseRedirect(model.get_absolute_url())
    else:
        form = TopicForm(instance=topic)

    return render_to_response('topics/create.html',
                              {'form': form},
                              context_instance=RequestContext(request))

def topic_detail(request, tc_pk):
    topic = get_object_or_404(Topic, pk=tc_pk)
    is_edit = request.user.is_authenticated() and  request.user == topic.creater

    return render_to_response('topics/tc_detail.html',
                              {'topic': topic,
                               'is_edit': is_edit},
                              context_instance=RequestContext(request))
