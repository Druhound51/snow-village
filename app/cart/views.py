# coding=utf-8
import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from app.store.models import Product
from .models import Cart
from .forms import CartAddProductForm


# Добавление новых товаров
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    form = CartAddProductForm(request.POST)
    product = Product.objects.get(id=product_id)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product,
            quantity=cd['quantity'],
            update_quantity=cd['update']
        )
    # return HttpResponse(
    #     json.dumps(list({
    #         # 'total_price': str(Cart(request).get_total_price()),
    #         'cart': Cart(request).cart.values()
    #     })))
    return HttpResponse(json.dumps(list(Cart(request).cart.values())))

# Удаление товара и корзины
def cart_remove(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.remove(product)
    return redirect('cart:CartDetail')


# Просмотр корзины
def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={
                'quantity': item['quantity'],
                'update': True
            })
    return render(request, 'cart/detail.html', {'cart': cart})
