# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView

from app.cart.forms import CartAddProductForm
from app.cart.models import Cart
from app.store.models import Product


class ProductListView(TemplateView):
    template_name = 'store/products.html'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        context['cart'] = Cart(self.request)
        return context
