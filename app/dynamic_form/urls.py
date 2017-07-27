# coding=utf-8
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<extra>[0-9]+)/$', views.custom_form, name='form'),
]
