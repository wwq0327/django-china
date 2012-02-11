from django.contrib.comments.signals import comment_was_posted
from topics.models import Topic

def last_reply(sender, comment, **kwargs):
    if comment.is_public:
        t = Topic.objects.get(pk=comment.object_pk)
        t.last_reply = comment.submit_date
        t.save()


