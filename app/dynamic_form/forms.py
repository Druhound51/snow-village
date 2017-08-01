# coding=utf-8
from __future__ import print_function
from django import forms

from app.dynamic_form.models import  FormType


class CustomForm(forms.Form):
    def __init__(self, *args, **kwargs):
        extra = FormType.objects.filter(form=kwargs.pop('extra'))
        super(CustomForm, self).__init__(*args, **kwargs)

        for form in extra:
            if form.type == 'TEXT':
                self.fields['field_%s' %
                            form.id] = forms.CharField(label=form.name)
            elif form.type == 'INT':
                self.fields['field_%s' %
                            form.id] = forms.IntegerField(label=form.name)
