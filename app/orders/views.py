# coding=utf-8
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from app.cart.models import Cart
from app.store.models import Product
from app.dynamic_form.views import send_mail_content
from .forms import OrderCreateForm
from .models import OrderItem


def order_create_view(request):
    cart = Cart(request)
    form = OrderCreateForm()
    return render(request, 'orders/create.html', {'cart': cart, 'form': form})


def order_create(request):
    cart = Cart(request)
    form = OrderCreateForm(request.POST)
    if form.is_valid():
        order = form.save()
        for item in cart:
            OrderItem.objects.create(order=order,
                                     product=item['product'],
                                     price=item['price'],
                                     quantity=item['quantity'])
        context = {'obj': form.data, 'cart': cart,
                   'total_price': cart.get_total_price()}
        cart.clear()
        send_mail_content('2', context, order.email)
    return redirect('/order/created/')


def order_show_view(request):
    return render(request, 'orders/created.html', {})