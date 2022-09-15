from django.db import models


class Ordering(models.Model):
    number = models.PositiveIntegerField(verbose_name='№')
    order_number = models.PositiveBigIntegerField(verbose_name='заказ №')
    cost_dollars = models.PositiveIntegerField(verbose_name='стоимость,$')
    delivery_date = models.DateField(verbose_name='срок поставки')
    cost_rubles = models.FloatField(verbose_name='стоимость,₽')
