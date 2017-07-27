# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey
from meta.models import ModelMeta


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(
            published=True, is_active__lte=timezone.now())


class PublishedModel(models.Model):
    published = models.BooleanField(default=False,
                                    verbose_name=u'Опубликовано')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='Дата обновления')
    is_active = models.DateTimeField(verbose_name='Дата публикации')

    objects = models.Manager()
    get_published = PublishedManager()

    class Meta(object):
        abstract = True


class PageModel(ModelMeta, PublishedModel, models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    text = RichTextField(null=True, blank=True,
                         verbose_name='Текст (HTML-блок)')

    title_page = models.CharField(max_length=170, verbose_name='Title')
    description_page = models.TextField(blank=True, verbose_name='Description')
    keywords_page = models.TextField(blank=True, verbose_name='Keywords')

    _metadata = {
        'title': 'title_page',
        'description': 'description_page',
        'keywords': 'keywords_page',
    }

    class Meta(object):
        abstract = True

    class MPTTMeta(object):
        order_insertion_by = ['title']

        def __init__(self):
            pass


class Page(MPTTModel, PageModel):
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='Children', on_delete=models.CASCADE)
    identifier = models.CharField(max_length=255,
                                  verbose_name='Идентификатор для url')

    def __str__(self):
        return '{0} {1} {2}'.format(
            self.title,
            '(опубликован)' if self.published else '',
            self.slug)

    def __init__(self, *args, **kwargs):
        self.parent_id = None
        super(Page, self).__init__(*args, **kwargs)
        if self.pk:
            self._old_identifier = self.identifier
        else:
            self._old_identifier = None
        self._old_parent = self.parent_id

    def get_absolute_url(self):
        return reverse('pages', args=[self.slug])

    class Meta(object):
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
