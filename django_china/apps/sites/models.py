# -*- coding: utf-8 -*-

from django.db import models

from django.contrib.auth.models import User

class SiteCategory(models.Model):
    name = models.CharField(u'分类名', max_length=24, unique=True)
    creater = models.ForeignKey(User)

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return self.name

class CoolSites(models.Model):
    name = models.CharField(u'网站名', max_length=64, unique=True)
    site = models.URLField(u'网址', unique=True)
    category = models.ForeignKey(SiteCategory)
    about = models.TextField(u'网站简介', null=True, blank=True)
    creater = models.ForeignKey(User)
    pub_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return '%s: %s' % (self.name, self.site)

