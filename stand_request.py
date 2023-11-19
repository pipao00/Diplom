import configuration
import requests
import data



def post_new_order():  # Функция для отправки запроса на создание нового заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER,
                         json=data.order_body)



def get_track(track_id):# Функция для отправки запроса на получение заказа по его трек-номеру
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_BY_ID + "?t=" + str(track_id))