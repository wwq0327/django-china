# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, Http404, HttpResponseForbidden, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

from sites.models import SiteCategory, CoolSites
from sites.forms import SiteCategoryForm, CoolSitesForm

def index(request):
    """酷站首页面"""

    return render_to_response('sites/index.html',
                              {},
                              context_instance=RequestContext(request))

@login_required
def create(request):
    """登录用户可自行添加相关网站"""

    form = CoolSitesForm()

    return render_to_response('sites/create.html',
                              {'form': form},
                              context_instance=RequestContext(request))
