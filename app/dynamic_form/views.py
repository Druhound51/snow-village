# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.http import HttpResponse4

import json

from app.dynamic_form.forms import CustomForm
from app.dynamic_form.models import FormAnswer, Form, EmailTemplate


def custom_form(request, **kwargs):
    if request.method == 'POST':
        form = CustomForm(request.POST, **kwargs)
        if form.is_valid():
            form_class = Form.objects.get(id=kwargs['extra'])
            obj = FormAnswer(name=form_class, text=form.cleaned_data)
            try:
                send_mail_content(form_class.template_code, obj.text)
            except:
                return HttpResponse(json.dumps({'error': 'Failed to send email'}))
            obj.save()
        else: 
          return HttpResponse(json.dumps({'errors': form.errors}))
    return HttpResponse(json.dumps({}))


def send_mail_content(template_code, context, email=settings.FEEDBACK_EMAIL):
    email_template = EmailTemplate.objects.get(id=template_code)
    body = email_template.render_body(context)
    send_mail(email_template.subject,
              body,
              email_template.admin_email, [email],
              fail_silently=True, html_message=body)
