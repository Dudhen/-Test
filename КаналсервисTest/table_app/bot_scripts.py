from datetime import datetime
import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials


def get_document_data():
    """
    Функция получения данных из документа
    """
    CREDENTIALS_FILE = './table_app.json'
    spreadsheet_id = '1dmxxjzCoOS6zbp3gOPHw5nMxiN5JCyp85Gn2wqPd_s0'

    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                                   ['https://www.googleapis.com/auth/spreadsheets',
                                                                    'https://www.googleapis.com/auth/drive'])

    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)


    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A:D',
        majorDimension='ROWS'
    ).execute()
    return values


def get_overdue_orders():
    """
    Функция получения просроченных номеров заказа
    """
    document_data = get_document_data()
    list_overdue_orders = []
    for i_string_table in document_data['values'][1:]:
        if datetime.strptime(i_string_table[3], '%d.%m.%Y') < datetime.now():
            list_overdue_orders.append({i_string_table[1]: i_string_table[3]})
    return list_overdue_orders
