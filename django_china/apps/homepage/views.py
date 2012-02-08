# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, Http404, HttpResponseForbidden, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

def index(request):
    return render_to_response('homepage/index.html',
                              {},
                              context_instance=RequestContext(request))
