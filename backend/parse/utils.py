from xml.etree import ElementTree

import requests


def get_result(day: int, month: int, year: int) -> float:
    """
    Выполняет запрос к API Банка России.
    """

    if day < 10:
        day = '0%s' % day

    if month < 10:
        month = '0%s' % month

    try:
        # Выполняем запрос к API.
        get_xml = requests.get(
            'http://www.cbr.ru/scripts/XML_daily.asp?date_req=%s/%s/%s' % (day, month, year)
        )

        # Парсинг XML используя ElementTree
        structure = ElementTree.fromstring(get_xml.content)
    except Exception:
        return 0.0

    try:
        # Поиск курса доллара (USD ID: R01235)
        dollar = structure.find("./*[@ID='R01235']/Value")
        dollar = dollar.text.replace(',', '.')
    except Exception:
        dollar = 0.0
    return float(dollar)
