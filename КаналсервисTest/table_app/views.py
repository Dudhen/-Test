from decimal import Decimal
from django.views.generic import ListView
from table_app.bot_scripts import get_document_data
from table_app.models import ResultTable
from table_app.web_scripts import get_today_dollar_rate, get_schedule_data_and_data_base_update
import json


class TablePageView(ListView):
    """
    Представление для страницы с графиком суммы сроков поставки заказа,
    а так же таблицей и общей суммой по всем срокам
    """

    template_name = 'table_page.html'

    def get_context_data(self, **kwargs):
        """
        Метод получения контекста
        """
        context = super(TablePageView, self).get_context_data(**kwargs)
        dollar_rate = get_today_dollar_rate()
        document_data = get_document_data()
        schedule = get_schedule_data_and_data_base_update(document_data, dollar_rate)
        context['schedule_keys'] = json.dumps(list(schedule.keys()))
        context['schedule_values'] = json.dumps(list(schedule.values()))
        context['sum_values'] = Decimal(sum(list(schedule.values())))
        return context

    def get_queryset(self):
        """
        Метод получения данных из базы
        """
        queryset = ResultTable.objects.all()
        return queryset
