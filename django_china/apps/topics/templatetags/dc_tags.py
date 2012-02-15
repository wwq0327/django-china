from django import template

from haystack.query import SearchQuerySet

register = template.Library()

@register.filter
def more_like_this(topic, limit=None):
    try:
        sqs = SearchQuerySet().more_like_this(topic)
        if limit is not None:
            sqs = sqs[:limit]
    except AttributeError:
        sqs = []
    return sqs
