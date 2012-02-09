# -*- coding: utf-8 -*-

from django import forms

from topics.models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('node', 'title', 'content', )

    def save(self, user):
        model = Topic(
            title = self.cleaned_data['title'],
            node = self.cleaned_data['node'],
            content = self.cleaned_data['content'],
            creater = user)
        model.save()

        return model

