# coding=utf-8
from django.db import models
from django.template import Template, Context


class EmailTemplate(models.Model):
    subject = models.CharField(max_length=100, verbose_name='Тема')
    admin_email = models.EmailField(max_length=254, verbose_name='E-mail администратора')
    body = models.TextField(verbose_name='Тело')

    class Meta(object):
        verbose_name = u'Шаблон письма'
        verbose_name_plural = u'Шаблоны писем'

    def __unicode__(self):
        return self.subject

    @staticmethod
    def render_email_part(content, context):
        mail_template = Template(content)
        mail_context = Context(context)
        return mail_template.render(mail_context)

    def render_body(self, context):
        return self.render_email_part(self.body, context)


class Form(models.Model):
    name = models.CharField(verbose_name='Название формы', max_length=50)
    template_code = models.ForeignKey(EmailTemplate, verbose_name='Шаблон письма', max_length=255)

    def __str__(self):
        return u'{}'.format(self.name)

    class Meta(object):
        verbose_name = 'Форма'
        verbose_name_plural = 'Формы'


class FormType(models.Model):
    DEFAULT_TYPE = 'TEXT'
    CHOICES = (('TEXT', 'Текстовое поле'), ('INT', 'Числовое поле'))
    form = models.ForeignKey(Form, related_name='Forms', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название', max_length=255)
    type = models.CharField(verbose_name='Тип', max_length=50, choices=CHOICES, default=DEFAULT_TYPE)

    def __str__(self):
        return u'field_{}'.format(self.id)

    class Meta(object):
        verbose_name = 'Тип формы'
        verbose_name_plural = 'Тип формы'


class FormAnswer(models.Model):
    name = models.CharField(verbose_name='Название формы', max_length=50)
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    text = models.TextField(verbose_name="Ответ")

    def __str__(self):
        return u'{} - {}'.format(self.name, self.pk)

    class Meta(object):
        verbose_name = 'Ответы'
        verbose_name_plural = 'Ответы'
