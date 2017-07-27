# coding=utf-8
from __future__ import unicode_literals

from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    price = models.IntegerField(verbose_name='Цена')

    def __str__(self):
        return '{0}'.format(
            self.title)

    class Meta(object):
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'
