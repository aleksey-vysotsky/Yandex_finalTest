# Высоцкий Алексей 37-я когорта - финальный проект. Инженер по тестированию плюс
# Импортируем модуль data, в котором хранится тестовый набор данных (тело заказа order_body), 
# который будет использоваться для отправки запроса на создание заказа
import data

# Импортируем две функции из модуля sender_stand_request: create_order(), get_order()
from sender_stand_request import create_order, get_order

# Определяем функцию теста, для проверки «создание заказа -> получение данных заказа по трек-номеру»
def test_order_creation_and_retrieval():
    # Вызываем функцию create_order, передавая ей тело заказа (data.order_body)
    # в качестве аргумента. Функция отправляет POST-запрос на сервер для создания заказа.
    response = create_order(data.order_body)
    # Извлекаем трек-номер заказа из ответа сервера
    track_number = response.json().get("track")
    # Выводим в консоль сообщение с трек-номером созданного заказа.
    print("Заказ создан. Номер трека:", track_number)
    # Вызываем функцию get_order, отправляем GET-запрос для получения данных созданного заказа, 
    # используя трек-номер в качестве параметра.
    order_response = get_order(track_number)
    # Проверяем что ответ от сервера равен 200
    assert order_response.status_code == 200, f"Ошибка: {order_response.status_code}"
    # Преобразуем ответ сервера из json в словарь дынных заказа
    order_data = order_response.json()
    print("Данные заказа:")
    # Выводим в консоль полный словарь order_data (данные заказа), чтобы убедиться в корректной передаче данных
    print(order_data)