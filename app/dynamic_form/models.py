# coding=utf-8
from django.db import models


class Form(models.Model):
    name = models.CharField(verbose_name='Название формы', max_length=50)

    def __str__(self):
        return u'{}'.format(self.name)

    class Meta(object):
        verbose_name = 'Форма'
        verbose_name_plural = 'Формы'


class FormType(models.Model):
    DEFAULT_TYPE = 'TEXT'
    CHOICES = (('TEXT', 'TEXT'), ('INT', 'INT'),)
    form = models.ForeignKey(Form,
                             related_name='Forms',
                             on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название',
                            max_length=255)
    type = models.CharField(verbose_name='Тип',
                            max_length=50,
                            choices=CHOICES, default=DEFAULT_TYPE)

    def __str__(self):
        return u'field_{}'.format(self.id)

    class Meta(object):
        verbose_name = 'Тип формы'
        verbose_name_plural = 'Тип формы'


class FormAnswer(models.Model):
    form = models.ForeignKey(Form, verbose_name="Форма")
    name = models.CharField(verbose_name='Название формы', max_length=50)
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    text = models.TextField(verbose_name="Ответ")

    def __str__(self):
        return u'Форма - {}'.format(self.pk)

    class Meta(object):
        verbose_name = 'Ответы'
        verbose_name_plural = 'Ответы'
