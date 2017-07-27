# coding=utf-8
from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError
from django.contrib import messages
from django_mptt_admin.admin import DjangoMpttAdmin

from app.pages.models import Page


class PageAdminForm(forms.ModelForm):
    class Meta(object):
        model = Page
        fields = '__all__'

    def clean_identifier(self):
        identifier = self.cleaned_data.get('identifier', False)
        if identifier and not self.data.get('parent'):
            docs = Page.objects.filter(identifier=identifier).exclude(
                identifier=self.instance.identifier)
            for doc in docs:
                if doc.is_root_node():
                    raise ValidationError(
                        u'Уже есть корневой элемент с таким идентификатором!')
        return identifier


class PageAdmin(DjangoMpttAdmin, forms.ModelForm, admin.ModelAdmin):
    tree_auto_open = 0
    list_display = ('title',)
    search_fields = ('title',)
    ordering = ('title',)
    form = PageAdminForm
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'published', 'title', 'identifier', 'is_active', 'created_at',
                'updated_at', 'text'),
        }),
        ('SEO', {
            'classes': ('collapse',),
            'fields': ('title_page', 'description_page', 'keywords_page')
        }),
    )

    def save_model(self, request, obj, form, change):
        super(PageAdmin, self).save_model(request, obj, form, change)
        if obj.identifier != obj._old_identifier or obj._old_parent != obj.parent:
            descendants = obj.get_root().get_descendants(include_self=True)
            for descendant in descendants:
                descendant.slug = u'' + u'/'.join([doc.identifier for doc in
                                                   descendant.get_ancestors(
                                                       include_self=True)]) + u'/'
                descendant.save()
            messages.info(request, u"У {} документов обновлен Slug".format(
                len(descendants)))


admin.site.register(Page, PageAdmin)
