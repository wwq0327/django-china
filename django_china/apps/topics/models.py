# -*- coding: utf-8 -*-

import markdown
from django.db import models
from django.contrib.auth.models import User

class Node(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return '/topics/node%s/' % self.pk

class Topic(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    content_html = models.TextField(editable=False)
    creater = models.ForeignKey(User)
    node = models.ForeignKey(Node)
    pub_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    last_reply_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        return "Topic %s: %s" % (self.node.name, self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('tc_detail', (), {
            'tc_pk': self.pk
            })

    def save(self, *args, **kwargs):
        self.content_html = markdown.markdown(self.content)
        super(Topic, self).save(*args, **kwargs)

    def _get_topic_num(self):
        return self.all().count()

    ## def _get_topic_node_num(self, node_pk):

    ##     return self.node.all().count()
