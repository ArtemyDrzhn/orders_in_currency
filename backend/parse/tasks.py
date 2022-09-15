import datetime

import gspread
import telepot
from django.conf import settings

from core.celery_app import app
from parse import contants
from parse.models import Ordering
from parse.utils import get_result


@app.task
def create_data():
    """
    Запись данных из google sheets в таблицу БД
    """
    gc = gspread.service_account(filename='test-362319-09d0def170c5.json')
    data = gc.open('test').sheet1.get_all_records()
    Ordering.objects.all().delete()

    for item in data:
        delivery_date = datetime.datetime.strptime(item.get(contants.DELIVERY_DAY), '%d.%m.%Y').date()
        dollar = get_result(day=delivery_date.day, month=delivery_date.month, year=delivery_date.year)
        obj = {
            'number': item.get(contants.NUMBER),
            'order_number': item.get(contants.ORDER_NUMBER),
            'cost_dollars': item.get(contants.COST_DOLLARS),
            'delivery_date': delivery_date,
            'cost_rubles': item.get(contants.COST_DOLLARS) * dollar,
        }
        Ordering.objects.create(**obj)


@app.task
def send_message():
    telegram_bot = telepot.Bot(settings.BOT_TOKEN)
    user_ids = {i['message']['chat']['id'] for i in telegram_bot.getUpdates()}
    for item in Ordering.objects.all():
        if item.delivery_date < datetime.datetime.now().date():
            for user_id in user_ids:
                telegram_bot.sendMessage(
                    chat_id=user_id,
                    text=f'Для *заказа № {item.order_number}* дата *{item.delivery_date}* истекла',
                    parse_mode='Markdown'
                )
