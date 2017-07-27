# coding=utf-8
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from app.cart.models import Cart
# from app.feedback.models import EmailTemplate
# TODO Create feedback form
from .forms import OrderCreateForm
from .models import OrderItem

EMAIL_TEMPLATES = {
    'orderseminar': 'orderseminar',
}


def order_create_view(request):
    cart = Cart(request)
    form = OrderCreateForm()
    return render(request, 'orders/create.html', {'cart': cart,
                                                 'form': form})


def order_create(request):
    cart = Cart(request)
    form = OrderCreateForm(request.POST)
    if form.is_valid():
        order = form.save()
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'],
                                     price=item['price'],
                                     quantity=item['quantity'])
        context = {'obj': form.data, 'cart': cart,
                   'total_price': cart.get_total_price()}
        cart.clear()
        # send_mail_content('orderseminar', context)
    return redirect('/order/created/')


def order_show_view(request):
    return render(request, 'orders/created.html', {})


# def send_mail_content(template_code, context):
#     email_template = EmailTemplate.objects.get(
#         identifier=EMAIL_TEMPLATES[template_code])
#     body = email_template.render_body(context)
#     send_mail(email_template.subject, body,
#               settings.SERVER_EMAIL, [settings.FEEDBACK_EMAIL],
#               fail_silently=True, html_message=body)
