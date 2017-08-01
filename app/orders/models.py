# coding=utf-8
from django.db import models

from app.store.models import Product


class Order(models.Model):
    CHOISE = (
        ('Мужчина', 'Мужчина'),
        ('Женщина', 'Женщина')
    )
    name = models.CharField(verbose_name='Контактное лицо', max_length=100)
    gender = models.CharField(verbose_name='Пол', choices=CHOISE,
                              default='Мужчина',
                              max_length=100)
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(verbose_name='phone', max_length=100)
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Обновлен', auto_now=True)

    class Meta(object):
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ: {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items')
    product = models.ForeignKey(Product, verbose_name='Товар', max_length=255)
    price = models.DecimalField(verbose_name='Цена', max_digits=255,
                                decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Количество',
                                           default=1)

    def __str__(self):
        return '{}: {}'.format(self.product, self.id)

    def get_cost(self):
        return self.price * self.quantity
