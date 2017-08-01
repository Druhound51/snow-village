# coding=utf-8
from __future__ import unicode_literals
import ast
from django.contrib import admin
from django.utils.safestring import mark_safe

from app.dynamic_form.models import Form, FormType, FormAnswer, EmailTemplate


class FormTypeInline(admin.TabularInline):
    model = FormType
    extra = 1
    raw_id_field = ['type']


class FormAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = (FormTypeInline,)


# class FormsAnswerAdmin(admin.ModelAdmin):
#     change_form_template = 'admin/dynamic_form/formsanswer/answer.html'
#
#     def change_view(self, request, object_id, form_url='', extra_context=None):
#         extra_context = extra_context or {}
#         obj = FormsAnswer.objects.get(pk=object_id)
#         _dict = ast.literal_eval(obj.text)
#         extra_context['FormsAnswer'] = _dict.items()
#
#         return super(FormsAnswerAdmin, self).change_view(
#             request,
#             object_id,
#             form_url,
#             extra_context=extra_context)

class FormAnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    fields = [
        'name',
        'text_field',
    ]
    readonly_fields = ['text_field', 'name']

    def save_model(self, request, obj, form, change):
        pass

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def text_field(self, obj):
        html = ''
        form_types_item = {}
        _dict = ast.literal_eval(obj.text)
        form_types = FormType.objects.values('id', 'name')
        for item in form_types:
            form_types_item[item["id"]] = item["name"]

        for key, value in _dict.items():
            form_key = key.split("_")[1]
            html += "<strong>{}</strong>: {}<br>".format(
                form_types_item[int(form_key)], value)
        return mark_safe(html)
    text_field.short_description = 'Текстовое поле'


class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ('subject',)


admin.site.register(Form, FormAdmin)
admin.site.register(FormAnswer, FormAnswerAdmin)
admin.site.register(EmailTemplate, EmailTemplateAdmin)
