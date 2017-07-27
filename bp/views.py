# coding=utf-8
from django.shortcuts import redirect
from django.views.generic import TemplateView


from app.dynamic_form.forms import CustomForm
from app.dynamic_form.models import FormAnswer, Form


class IndexView(TemplateView):
    template_name = 'base.html'
    context_object_name = 'index'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        return context

