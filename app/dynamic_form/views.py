# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from app.dynamic_form.forms import CustomForm
from app.dynamic_form.models import FormAnswer, Form


def custom_form(request,  extra, **kwargs):
    if request.method == 'POST':
        kwargs['extra'] = extra
        form = CustomForm(request.POST, **kwargs)
        if form.is_valid():
            obj = FormAnswer(name="Форма",
                             text=form.cleaned_data,
                             form=Form(id=extra))
            obj.save()
    return redirect('index')
