import requests
import xmltodict
from datetime import datetime
from table_app.models import ResultTable


def get_today_dollar_rate():
    """
    Функция получения курса доллара к рублю
    """
    date_req = {'date_req': datetime.strftime(datetime.now(), '%d/%m/%Y')}
    response = requests.get('https://www.cbr.ru/scripts/XML_daily.asp', date_req)
    dollar_rate = float([i_value['Value'] for i_value in xmltodict.parse(response.content)['ValCurs']['Valute']
                         if i_value['CharCode'] == 'USD'][0].replace(',', '.'))
    return dollar_rate


def get_schedule_data_and_data_base_update(document_data, dollar_rate):
    """
    Функция получения данных для графика,
    а так же обновления базы данных
    """
    ResultTable.objects.all().delete()
    new_table_strings = []
    schedule = {}
    for i_string_table in document_data['values'][1:]:
        new_table_strings.append(ResultTable(
            id=int(i_string_table[0]),
            order_number=int(i_string_table[1]),
            price_dollars=float(i_string_table[2]),
            delivery_date=datetime.strptime(i_string_table[3], '%d.%m.%Y'),
            price_rubs=float(i_string_table[2]) * dollar_rate
        ))
        if i_string_table[3] in schedule:
            schedule[i_string_table[3]] = float(schedule[i_string_table[3]]) + float(i_string_table[2])
        else:
            schedule[i_string_table[3]] = float(i_string_table[2])
    ResultTable.objects.bulk_create(new_table_strings)

    return schedule
