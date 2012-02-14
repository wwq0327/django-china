# -*- coding: utf-8 -*-

import datetime
import markdown

from django.db import models
from django.db.models import Q

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db.models import F

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

class TopicManager(models.Manager):
    def get_related_topics(self, num=10, title=None):
        return self.get_query_set().filter(Q(title__icontains=title)|Q(content__icontains=title))[0:num]

class Topic(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    content_html = models.TextField(editable=False)
    creater = models.ForeignKey(User)
    node = models.ForeignKey(Node, verbose_name=u'节点') # verbose_name 字段自述名
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    last_reply = models.DateTimeField(editable=False, null=True, blank=True)
    comments_count = models.IntegerField(editable=False, null=True, blank=True, default=0)

    objects = TopicManager()

    class Meta:
        ordering = ['-last_reply']

    def __unicode__(self):
        return "Topic %s: %s" % (self.node.name, self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('tc_detail', (), {
            'tc_pk': self.pk
            })




    ## ## 代参来自： http://djangosnippets.org/snippets/108/
    ## def most_commented(self, num=5):
    ##     """
    ##     Returns the ``num`` objects with the highest comment counts,
    ##     in order.

    ##     Pass ``free=False`` if you're using the registered comment
    ##     model (Comment) instead of the anonymous comment model
    ##     (FreeComment).

    ##     """
    ##     from django.db import connection
    ##     from django.contrib.comments import models as comment_models
    ##     from django.contrib.contenttypes.models import ContentType
    ##     ## if free:
    ##     ##     comment_opts = comment_models.FreeComment._meta
    ##     ## else:
    ##     ##     comment_opts = comment_models.Comment._meta
    ##     comment_opts = comment_models.Comment._meta
    ##     ctype = ContentType.objects.get_for_model(self.model)
    ##     query = """SELECT object_id, COUNT(*) AS score
    ##     FROM %s
    ##     WHERE content_type_id = %%s
    ##     AND is_public = 1
    ##     GROUP BY object_id
    ##     ORDER BY score DESC""" % comment_opts.db_table

    ##     cursor = connection.cursor()
    ##     cursor.execute(query, [ctype.id])
    ##     object_ids = [row[0] for row in cursor.fetchall()[:num]]

    ##     # Use ``in_bulk`` here instead of an ``id__in`` filter, because ``id__in``
    ##     # would clobber the ordering.
    ##     object_dict = self.in_bulk(object_ids)

    ##     return [object_dict[object_id] for object_id in object_ids]


    def save(self, *args, **kwargs):
        if self.pk is None:
            self.last_reply = datetime.datetime.now()

        self.content_html = markdown.markdown(self.content)
        super(Topic, self).save(*args, **kwargs)

def user_count():
    '''获取总会员数'''
    return User.objects.all().count()

def comments_count():
    '''获取总评论数'''
    topic_type = ContentType.objects.get(app_label="topics", model="topic")
    comments = Comment.objects.filter(content_type=topic_type)
    return comments.count()

def top_comments(num=10):
    from django.contrib.comments import models as comment_models
    comment_opts = comment_models.Comment._meta
    comment_table_name = comment_opts.db_table

    ctype = ContentType.objects.get(app_label="topics", model="topic")

    return Topic.objects.extra(
        select={
            'c_count': 'SELECT COUNT(*) FROM %s WHERE content_type_id = %s AND is_public = 1' % (comment_table_name, ctype.id)},
        ).order_by('-c_count')[0:num]

# 让comment 与 topic通信，当有新的评论产生后，
# 则在topic中修改最后回复时间
def last_reply(sender, comment, **kwargs):
    if comment.is_public:
        t = Topic.objects.get(pk=comment.object_pk)
        t.last_reply = comment.submit_date
        t.comments_count = F('comments_count') + 1
        t.save()

comment_was_posted.connect(last_reply, sender=Comment)
