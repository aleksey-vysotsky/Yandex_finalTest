# Импортируем модуль configuration где содержаться данные конечного URL сервера и ручек API
import configuration
# Импортируем библиотеку requests для отправки HTTP-запросов
import requests
# Импортируем модуль data, в котором хранится тестовый набор данных (тело заказа order_body), 
# который будет использоваться для отправки запроса на создание заказа
import data

# Создаем функцию для отправки POST-запросов, для создания заказа
def create_order(body):
    return requests.post(configuration.URL_SERVICE+configuration.CREATE_ORDERS,
                         json=body,
                         headers=data.headers)

# Создаем функцию для отправки GET-запросов, для получения информации о заказе по трек-номеру
def get_order(track_number):
    get_order_url = (
        configuration.URL_SERVICE +
        configuration.GET_ORDER_BY_TRACK +
        f"?t={track_number}"
    )
    response = requests.get(get_order_url)
    return response