# -*- coding: utf-8 -*-

import datetime
import markdown

from django.db import models
from django.contrib.auth.models import User

from django.contrib.comments.models import Comment
from django.contrib.comments.signals import comment_was_posted
#from topics.signals import last_reply

class Node(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

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
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    last_reply = models.DateTimeField(editable=False, null=True, blank=True)

    class Meta:
        ordering = ['-last_reply']

    def __unicode__(self):
        return "Topic %s: %s" % (self.node.name, self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('tc_detail', (), {
            'tc_pk': self.pk
            })

    def save(self, *args, **kwargs):
        if not self.pk:
            self.last_reply = datetime.datetime.now()

        self.content_html = markdown.markdown(self.content)
        super(Topic, self).save(*args, **kwargs)

    ## def _get_topic_num(self):
    ##     return self.all().count()

    ## def _get_topic_node_num(self, node_pk):

    ##     return self.node.all().count()

def last_reply(sender, comment, **kwargs):
    if comment.is_public:
        t = Topic.objects.get(pk=comment.object_pk)
        t.last_reply = comment.submit_date
        t.save()

comment_was_posted.connect(last_reply, sender=Comment)
