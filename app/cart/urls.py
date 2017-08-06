# coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^remove/(?P<product_id>[^/]*)/$', views.cart_remove,
        name='CartRemove'),
    url(r'^add/(?P<product_id>[^/]*)/$', views.cart_add, name='CartAdd'),
]
