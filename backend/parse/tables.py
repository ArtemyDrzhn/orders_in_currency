import django_tables2 as tables

from parse.models import Ordering


class OrderingTable(tables.Table):
    class Meta:
        model = Ordering
        template_name = 'django_tables2/bootstrap.html'
        fields = ('number', 'order_number', 'cost_dollars', 'delivery_date', 'cost_rubles')
