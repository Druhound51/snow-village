# coding=utf-8
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^view/$', views.order_create_view, name='OrderCreateView'),
    url(r'^created/$', views.order_show_view, name="OrderShowView"),
    url(r'^create/$', views.order_create, name='OrderCreate'),
]
