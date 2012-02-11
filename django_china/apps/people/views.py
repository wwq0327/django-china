# -*- coding: utf-8 -*-

from django.conf import settings
from django.http import HttpResponseRedirect, Http404, HttpResponseForbidden
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

## from tagging.models import Tag
## from tagging.utils import calculate_cloud, LOGARITHMIC

from django.contrib.auth.models import User
## from feed.models import ReadFeed, Share, Star
## from friendships.models import Friendship

@login_required
def index(request, username):

    c_user = get_object_or_404(User, username=username)
    ## if c_user == request.user:
    ##     feed_list = c_user.readfeed_set.all()
    ## else:
    ##     feed_list = c_user.readfeed_set.filter(secret=False)

    ## star_list = c_user.star_set.all()[:10]
    ## share_list = c_user.share_set.all()[:10]
    ## tags = Tag.objects.usage_for_model(ReadFeed,
    ##                                    counts=True,
    ##                                    filters=dict(creater__username=username))
    ## clouds = calculate_cloud(tags, steps=settings.TAG_LIST_LEVEL, distribution=LOGARITHMIC)

    profile = c_user.get_profile()

    ## is_friend = Friendship.objects.filter(from_friend=request.user,
    ##                                       to_friend=c_user)

    return render_to_response('people/index.html',
                              {'c_user': c_user,
                               ## 'feed_list': feed_list,
                               ## 'star_list': star_list,
                               ## 'share_list': share_list,
                               ## 'tags': tags,
                               ## 'clouds': clouds,
                               'profile': profile,
                               ## 'is_friend': is_friend,
                               },
                              context_instance=RequestContext(request))
