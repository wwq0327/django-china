from django import forms
from django.contrib.auth.models import User

from coolsites.models import SiteCategory, CoolSites

class SiteCategoryForm(forms.ModelForm):
    class Meta:
        model = SiteCategory

    def save(self, user):
        model, created = SiteCategory.objects.get_or_create(
            name = self.cleaned_data['name'],
            creater = user)

        if created:
            model.save()

        return model

class CoolSitesForm(forms.ModelForm):
    class Meta:
        model = CoolSites
        fields = ('name', 'site', 'category', 'about', )

    def save(self, user):
        model, created = CoolSites.objects.get_or_create(
            name = self.cleaned_data['name'],
            sites = self.cleaned_data['site'],
            category = self.cleaned_data['category'],
            about = self.cleaned_data['about'],
            creater = user
            )

        if created:
            model.save()

        return model
