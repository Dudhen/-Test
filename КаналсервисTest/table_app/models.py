from django.db import models


def validate_decimals(value):
    """
    Функция валидации данных в столбце с ценами
    """
    return f'{float(value):.{2}f}'


class ResultTable(models.Model):
    """
    Модель таблицы заказов
    """
    id = models.IntegerField(verbose_name='№', primary_key=True)
    order_number = models.IntegerField(verbose_name='заказ №')
    price_dollars = models.DecimalField(verbose_name='стоимость,$', decimal_places=2, max_digits=20)
    delivery_date = models.DateField(auto_now_add=False, verbose_name='срок поставки')
    price_rubs = models.DecimalField(verbose_name='стоимость в руб.', decimal_places=2, max_digits=20)

