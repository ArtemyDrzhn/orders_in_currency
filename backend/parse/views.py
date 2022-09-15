from django.db.models import Sum
from django.views.generic import ListView
from django_tables2 import SingleTableMixin

from parse.models import Ordering
from parse.tables import OrderingTable


class OrderingListView(SingleTableMixin, ListView):
    model = Ordering
    table_class = OrderingTable
    template_name = 'parse/ordering.html'

    def get_table_pagination(self, table) -> bool:
        """
        Отключение пагинации
        """
        return False

    def get_context_data(self, **kwargs) -> dict:
        """
        Вычисление общей суммы в долларах
        """
        data = super().get_context_data(**kwargs)
        total_sum = self.get_queryset().aggregate(sum=Sum('cost_dollars'))
        data.update(total_sum)
        return data
