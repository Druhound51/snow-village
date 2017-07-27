# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')

    fieldsets = (
        (None, {
            'fields': (
                'title', 'price'),
        }),
    )


admin.site.register(Product, ProductAdmin)
